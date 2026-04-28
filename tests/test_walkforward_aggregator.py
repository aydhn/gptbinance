import pytest
from app.backtest.walkforward.aggregator import OOSAggregator
from app.backtest.walkforward.models import (
    WalkForwardSegmentResult,
    WalkForwardWindow,
    WindowDiagnostic,
)
from app.backtest.walkforward.enums import SegmentStatus
from app.backtest.models import (
    BacktestResult,
    PerformanceSummary,
    BacktestConfig,
    BacktestRun,
)
from datetime import datetime
from uuid import uuid4


def _make_segment(
    index: int, status: SegmentStatus, return_pct: float, trades: int, dd: float
) -> WalkForwardSegmentResult:
    win = WalkForwardWindow(
        segment_index=index,
        is_start=0,
        is_end=10,
        oos_start=10,
        oos_end=20,
        is_length=10,
        oos_length=10,
        is_valid=True,
    )
    if status != SegmentStatus.COMPLETED:
        return WalkForwardSegmentResult(segment_index=index, window=win, status=status)

    perf = PerformanceSummary(
        run_id="test",
        total_trades=trades,
        winning_trades=int(trades * 0.5),
        losing_trades=int(trades * 0.5),
        total_return_pct=return_pct,
        win_rate=0.5,
        max_drawdown_pct=dd,
        sharpe_ratio=1.0,
        sortino_ratio=1.0,
        expectancy=return_pct / trades if trades > 0 else 0,
        max_consecutive_wins=2,
        max_consecutive_losses=2,
        avg_win=1.0,
        avg_loss=0.5,
    )
    cfg = BacktestConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_time=datetime(2023, 1, 1),
        end_time=datetime(2023, 2, 1),
        strategy_set="strat1",
    )
    run = BacktestRun(
        run_id=str(uuid4()),
        config=cfg,
        started_at=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    res = BacktestResult(run=run, summary=perf)

    return WalkForwardSegmentResult(
        segment_index=index, window=win, status=status, oos_result=res
    )


def test_aggregator():
    segments = [
        _make_segment(1, SegmentStatus.COMPLETED, return_pct=10.0, trades=10, dd=0.05),
        _make_segment(2, SegmentStatus.COMPLETED, return_pct=-5.0, trades=5, dd=0.10),
        _make_segment(3, SegmentStatus.FAILED, return_pct=0.0, trades=0, dd=0.0),
    ]

    aggregator = OOSAggregator()
    res = aggregator.aggregate(segments)

    assert res.total_segments == 3
    assert res.completed_segments == 2
    assert res.total_oos_trades == 15
    assert res.aggregate_oos_return == 5.0
    assert res.aggregate_oos_max_drawdown == 0.10
    assert len(res.segment_summaries) == 3

    # Check that failed segment is handled
    assert res.segment_summaries[2].status == SegmentStatus.FAILED.value
    assert res.segment_summaries[2].oos_trades == 0
