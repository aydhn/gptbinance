from typing import List
from app.backtest.validation.models import (
    BenchmarkResult,
    ComparisonResult,
    ComparisonMetricRow,
    ComparisonVerdict,
)
from app.backtest.models import PerformanceSummary as BacktestSummary
from app.backtest.validation.base import ComparisonEvaluatorBase


class MetricComparisonEvaluator(ComparisonEvaluatorBase):
    def compare(
        self, strategy_summary: BacktestSummary, benchmark_result: BenchmarkResult
    ) -> ComparisonResult:
        metrics = []

        # Helper to calc diffs
        def calc_row(
            name: str, strat_val: float, bench_val: float, higher_is_better: bool
        ) -> ComparisonMetricRow:
            abs_diff = strat_val - bench_val
            rel_diff = (abs_diff / abs(bench_val)) * 100 if bench_val != 0 else 0.0

            # if both are 0, it's not better or worse, just equal. We'll say is_better=True if abs_diff >= 0 (for higher_is_better)
            if higher_is_better:
                is_better = abs_diff > 0
            else:
                is_better = abs_diff < 0

            return ComparisonMetricRow(
                metric_name=name,
                strategy_value=strat_val,
                benchmark_value=bench_val,
                absolute_diff=abs_diff,
                relative_diff_pct=rel_diff,
                is_better=is_better,
            )

        # Assuming summary has these attributes based on previous phases
        strat_metrics = strategy_summary
        bench_metrics = benchmark_result.summary

        total_ret_row = calc_row(
            "Total Return (%)",
            getattr(strat_metrics, "total_return_pct", 0),
            getattr(bench_metrics, "total_return_pct", 0),
            True,
        )
        max_dd_row = calc_row(
            "Max Drawdown (%)",
            getattr(strat_metrics, "max_drawdown_pct", 0),
            getattr(bench_metrics, "max_drawdown_pct", 0),
            False,
        )
        win_rate_row = calc_row(
            "Win Rate (%)",
            getattr(strat_metrics, "win_rate_pct", 0),
            getattr(bench_metrics, "win_rate_pct", 0),
            True,
        )
        profit_factor_row = calc_row(
            "Profit Factor",
            getattr(strat_metrics, "profit_factor", 0),
            getattr(bench_metrics, "profit_factor", 0),
            True,
        )
        trade_count_row = calc_row(
            "Trade Count",
            getattr(strat_metrics, "total_trades", 0),
            getattr(bench_metrics, "total_trades", 0),
            True,
        )  # debatable if higher is better, but keeps logic simple

        metrics.extend(
            [
                total_ret_row,
                max_dd_row,
                win_rate_row,
                profit_factor_row,
                trade_count_row,
            ]
        )

        # Verdict logic
        # Very simplistic logic for phase 10: outpeform if total return AND max DD are better
        verdict = ComparisonVerdict.INCONCLUSIVE
        if total_ret_row.is_better and max_dd_row.is_better:
            verdict = ComparisonVerdict.OUTPERFORM
        elif not total_ret_row.is_better and not max_dd_row.is_better:
            verdict = ComparisonVerdict.UNDERPERFORM
        else:
            verdict = ComparisonVerdict.MARGINAL

        caveat = None
        if trade_count_row.strategy_value < 10:
            caveat = "Strategy has very few trades (<10). Comparison may be statistically insignificant."

        return ComparisonResult(
            strategy_run_id=strategy_summary.run_id,
            benchmark_run_id=benchmark_result.spec.benchmark_id,
            metrics=metrics,
            verdict=verdict,
            caveat=caveat,
        )
