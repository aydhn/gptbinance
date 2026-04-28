import pytest
from app.backtest.walkforward.promotion_gates import PromotionGateEvaluator
from app.backtest.walkforward.models import WalkForwardAggregateResult
from app.backtest.walkforward.enums import AggregateVerdict


def test_promotion_gates_pass():
    agg = WalkForwardAggregateResult(
        total_segments=5,
        completed_segments=5,
        total_oos_trades=50,
        aggregate_oos_return=10.0,
        aggregate_oos_expectancy=0.5,
        aggregate_oos_max_drawdown=0.1,
        segment_summaries=[],
    )

    evaluator = PromotionGateEvaluator(
        min_segments=3, min_trades=10, min_expectancy=0.0
    )
    res = evaluator.evaluate(agg)

    assert res.verdict == AggregateVerdict.PASS
    assert len(res.checks) == 3


def test_promotion_gates_fail_expectancy():
    agg = WalkForwardAggregateResult(
        total_segments=5,
        completed_segments=5,
        total_oos_trades=50,
        aggregate_oos_return=-10.0,
        aggregate_oos_expectancy=-0.5,
        aggregate_oos_max_drawdown=0.1,
        segment_summaries=[],
    )

    evaluator = PromotionGateEvaluator(
        min_segments=3, min_trades=10, min_expectancy=0.0
    )
    res = evaluator.evaluate(agg)

    assert res.verdict == AggregateVerdict.FAIL
    assert any(c["status"] == "fail" for c in res.checks)
