import pytest
from app.backtest.walkforward.reporting import WalkForwardReporter
from app.backtest.walkforward.models import (
    WalkForwardAggregateResult,
    PromotionGateResult,
    WindowPerformanceSummary,
)
from app.backtest.walkforward.enums import AggregateVerdict


def test_reporting():
    agg = WalkForwardAggregateResult(
        total_segments=1,
        completed_segments=1,
        total_oos_trades=10,
        aggregate_oos_return=5.0,
        aggregate_oos_expectancy=0.5,
        aggregate_oos_max_drawdown=0.1,
        segment_summaries=[
            WindowPerformanceSummary(
                segment_index=1,
                status="completed",
                oos_trades=10,
                oos_total_return=5.0,
                oos_expectancy=0.5,
                oos_max_drawdown=0.1,
            )
        ],
    )
    gates = PromotionGateResult(verdict=AggregateVerdict.PASS, checks=[], summary="ok")

    reporter = WalkForwardReporter()
    summary_str = reporter.format_summary(agg, gates)
    segments_str = reporter.format_segments(agg)
    diag_str = reporter.format_diagnostics(["Warning 1"])

    assert "WALK-FORWARD SUMMARY" in summary_str
    assert "PASS" in summary_str
    assert "SEGMENT OOS PERFORMANCE" in segments_str
    assert "Warning 1" in diag_str
