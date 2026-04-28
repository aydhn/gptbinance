import pytest
from app.backtest.walkforward.segment_runner import SegmentRunner
from app.backtest.walkforward.selection import CandidateSelector
from app.backtest.walkforward.freeze import FreezeManager
from app.backtest.walkforward.models import WalkForwardConfig, WalkForwardWindow
from app.backtest.walkforward.enums import WindowScheme, SegmentStatus, PromotionVerdict
from app.backtest.models import (
    BacktestResult,
    PerformanceSummary,
    BacktestConfig,
    BacktestRun,
)
from app.strategies.models import StrategySpec
from app.strategies.enums import StrategyType
from uuid import uuid4
from datetime import datetime


def _mock_run_backtest(config: BacktestConfig) -> BacktestResult:
    perf = PerformanceSummary(
        run_id="test",
        total_trades=10,
        winning_trades=5,
        losing_trades=5,
        total_return=0.5,
        win_rate=0.5,
        max_drawdown_pct=0.1,
        sharpe_ratio=1.0,
        sortino_ratio=1.0,
        expectancy=0.5,
        max_consecutive_wins=2,
        max_consecutive_losses=2,
        avg_win=1.0,
        avg_loss=0.5,
    )
    run = BacktestRun(
        run_id=str(uuid4()),
        config=config,
        started_at=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return BacktestResult(run=run, summary=perf)


def test_segment_runner_skipped_invalid_window():
    selector = CandidateSelector()
    freezer = FreezeManager()
    runner = SegmentRunner(selector, freezer, _mock_run_backtest)

    config = WalkForwardConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_ts=0,
        end_ts=10000,
        feature_set="core",
        strategy_set="core",
        window_scheme=WindowScheme.ROLLING,
        is_bars=50,
        oos_bars=20,
        step_bars=20,
    )

    window = WalkForwardWindow(
        segment_index=1,
        is_start=0,
        is_end=10,
        oos_start=10,
        oos_end=20,
        is_length=10,
        oos_length=10,
        is_valid=False,
        reason="Too short",
    )

    specs = [
        StrategySpec(
            name="strat1", strategy_type=StrategyType.TREND_FOLLOW, required_features=[]
        )
    ]

    res = runner.run_segment(config, window, specs)

    assert res.status == SegmentStatus.SKIPPED_INSUFFICIENT_DATA
    assert res.error_message == "Too short"


def test_segment_runner_success():
    selector = CandidateSelector()
    freezer = FreezeManager()
    runner = SegmentRunner(selector, freezer, _mock_run_backtest)

    config = WalkForwardConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_ts=0,
        end_ts=10000,
        feature_set="core",
        strategy_set="core",
        window_scheme=WindowScheme.ROLLING,
        is_bars=50,
        oos_bars=20,
        step_bars=20,
    )

    window = WalkForwardWindow(
        segment_index=1,
        is_start=0,
        is_end=50,
        oos_start=50,
        oos_end=70,
        is_length=50,
        oos_length=20,
        is_valid=True,
    )

    specs = [
        StrategySpec(
            name="strat1", strategy_type=StrategyType.TREND_FOLLOW, required_features=[]
        )
    ]

    res = runner.run_segment(config, window, specs)

    assert res.status == SegmentStatus.COMPLETED
    assert res.selection is not None
    assert res.selection.verdict == PromotionVerdict.PROMOTED
    assert res.oos_result is not None
    assert res.diagnostics is not None
    assert (
        res.diagnostics.expectancy_decay == 0.0
    )  # Mock returns same expectancy for IS and OOS
