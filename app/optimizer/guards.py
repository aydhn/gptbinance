from typing import List, Optional
from app.optimizer.base import BaseGuardEvaluator
from app.optimizer.models import OptimizationGuardReport, GuardWarning, TrialMetrics
from app.optimizer.enums import GuardSeverity, PruningVerdict


class StandardGuardEvaluator(BaseGuardEvaluator):
    def evaluate(self, trial_id: str, metrics: TrialMetrics) -> OptimizationGuardReport:
        warnings: List[GuardWarning] = []

        if metrics.total_trades < 5:
            warnings.append(
                GuardWarning(
                    severity=GuardSeverity.FAIL,
                    code="EXTREME_LOW_TRADES",
                    message="Extremely low trade count. Highly susceptible to overfitting.",
                    recommended_handling="Prune immediately. Do not use for live trading.",
                    metric="total_trades",
                    value=metrics.total_trades,
                )
            )
        elif metrics.total_trades < 20:
            warnings.append(
                GuardWarning(
                    severity=GuardSeverity.WARNING,
                    code="LOW_TRADES",
                    message="Low trade count. Statistical significance is questionable.",
                    recommended_handling="Penalize score heavily. Review individual trades.",
                    metric="total_trades",
                    value=metrics.total_trades,
                )
            )

        if metrics.expectancy > 0.5 and metrics.max_drawdown_pct > 30.0:
            warnings.append(
                GuardWarning(
                    severity=GuardSeverity.WARNING,
                    code="OBJECTIVE_GAMING_DD",
                    message="High expectancy achieved alongside massive drawdown.",
                    recommended_handling="Penalize score. Likely surviving huge swings by luck.",
                    metric="max_drawdown_pct",
                    value=metrics.max_drawdown_pct,
                )
            )

        if metrics.benchmark_relative_strength < -0.2:
            warnings.append(
                GuardWarning(
                    severity=GuardSeverity.CAUTION,
                    code="WEAK_BENCHMARK",
                    message="Significantly underperforming a simple buy-and-hold benchmark.",
                    recommended_handling="Caution. Strategy may not justify its complexity.",
                    metric="benchmark_relative_strength",
                    value=metrics.benchmark_relative_strength,
                )
            )

        pruning_verdict = PruningVerdict.KEEP
        for w in warnings:
            if w.severity == GuardSeverity.FAIL:
                pruning_verdict = PruningVerdict.PRUNE_GUARDS
                break

        passed_all = pruning_verdict == PruningVerdict.KEEP and not any(
            w.severity == GuardSeverity.WARNING for w in warnings
        )

        return OptimizationGuardReport(
            trial_id=trial_id,
            warnings=warnings,
            passed_all=passed_all,
            pruning_verdict=pruning_verdict,
        )
