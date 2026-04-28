import pytest
from app.backtest.walkforward.selection import CandidateSelector
from app.backtest.walkforward.models import WalkForwardConfig
from app.backtest.walkforward.enums import (
    WindowScheme,
    SelectionPolicy,
    PromotionVerdict,
)
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


def _make_result(
    name: str, trades: int, expectancy: float, dd: float
) -> BacktestResult:
    perf = PerformanceSummary(
        run_id="test",
        total_trades=trades,
        winning_trades=int(trades * 0.5),
        losing_trades=int(trades * 0.5),
        total_return=expectancy * trades,
        win_rate=0.5,
        max_drawdown_pct=dd,
        sharpe_ratio=1.0,
        sortino_ratio=1.0,
        expectancy=expectancy,
        max_consecutive_wins=2,
        max_consecutive_losses=2,
        avg_win=expectancy * 2,
        avg_loss=expectancy * 0.5,
    )
    cfg = BacktestConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_time=datetime(2023, 1, 1),
        end_time=datetime(2023, 2, 1),
        strategy_set=name,
    )
    run = BacktestRun(
        run_id=str(uuid4()),
        config=cfg,
        started_at=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return BacktestResult(run=run, summary=perf)


def test_selection_max_expectancy():
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
        selection_policy=SelectionPolicy.MAX_EXPECTANCY,
        min_trades_is=5,
    )

    results = [
        _make_result("strat1", trades=10, expectancy=0.5, dd=0.1),
        _make_result("strat2", trades=10, expectancy=1.2, dd=0.3),
        _make_result(
            "strat3", trades=2, expectancy=2.0, dd=0.05
        ),  # Rejected: low trades
        _make_result(
            "strat4", trades=10, expectancy=-0.5, dd=0.1
        ),  # Rejected: negative expectancy
    ]

    specs = {
        "strat1": StrategySpec(
            name="strat1", strategy_type=StrategyType.TREND_FOLLOW, required_features=[]
        ),
        "strat2": StrategySpec(
            name="strat2", strategy_type=StrategyType.TREND_FOLLOW, required_features=[]
        ),
    }

    selector = CandidateSelector()
    res = selector.select(config, results, specs)

    assert res.verdict == PromotionVerdict.PROMOTED
    assert res.selected_candidate is not None
    assert res.selected_candidate.spec.name == "strat2"


def test_selection_min_drawdown():
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
        selection_policy=SelectionPolicy.MIN_DRAWDOWN,
        min_trades_is=5,
    )

    results = [
        _make_result("strat1", trades=10, expectancy=0.5, dd=0.1),
        _make_result("strat2", trades=10, expectancy=1.2, dd=0.3),
    ]

    specs = {
        "strat1": StrategySpec(
            name="strat1", strategy_type=StrategyType.TREND_FOLLOW, required_features=[]
        ),
        "strat2": StrategySpec(
            name="strat2", strategy_type=StrategyType.TREND_FOLLOW, required_features=[]
        ),
    }

    selector = CandidateSelector()
    res = selector.select(config, results, specs)

    assert res.verdict == PromotionVerdict.PROMOTED
    assert res.selected_candidate.spec.name == "strat1"


def test_selection_no_valid_candidates():
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
        selection_policy=SelectionPolicy.MIN_DRAWDOWN,
        min_trades_is=5,
    )
    results = [
        _make_result("strat1", trades=2, expectancy=0.5, dd=0.1),
    ]
    specs = {}
    selector = CandidateSelector()
    res = selector.select(config, results, specs)

    assert res.verdict == PromotionVerdict.REJECTED
    assert res.selected_candidate is None
