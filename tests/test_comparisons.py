import pytest
import uuid
from app.backtest.validation.comparisons import MetricComparisonEvaluator
from app.backtest.models import PerformanceSummary as BacktestSummary
from app.backtest.validation.models import (
    BenchmarkResult,
    BenchmarkSpec,
    BaselineStrategyDescriptor,
)
from app.backtest.validation.enums import BenchmarkType, ComparisonVerdict


def test_metric_comparison():
    evaluator = MetricComparisonEvaluator()
    strat_summary = BacktestSummary(
        run_id=str(uuid.uuid4()),
        config_id=uuid.uuid4(),
        total_return_pct=20.0,
        max_drawdown_pct=10.0,
        total_trades=50,
        win_rate_pct=50,
        profit_factor=1.5,
    )

    bench_spec = BenchmarkSpec(
        run_id=str(uuid.uuid4()),
        benchmark_type=BenchmarkType.FLAT,
        baseline_descriptor=BaselineStrategyDescriptor(
            name="F", benchmark_type=BenchmarkType.FLAT, description=""
        ),
    )
    bench_summary = BacktestSummary(
        run_id=str(uuid.uuid4()),
        config_id=uuid.uuid4(),
        total_return_pct=20.0,
        max_drawdown_pct=10.0,
        total_trades=50,
        win_rate_pct=50,
        profit_factor=1.5,
    )
    bench_res = BenchmarkResult(spec=bench_spec, summary=bench_summary)

    comp = evaluator.compare(strat_summary, bench_res)
    assert comp.verdict in [
        ComparisonVerdict.MARGINAL,
        ComparisonVerdict.OUTPERFORM,
        ComparisonVerdict.UNDERPERFORM,
    ]
