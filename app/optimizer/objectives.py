from typing import Dict, Any
from app.optimizer.base import BaseScorer
from app.optimizer.models import ObjectiveScore, TrialMetrics
from app.optimizer.enums import ObjectiveComponent


class CompositeObjectiveScorer(BaseScorer):
    def __init__(self, min_trades: int = 10, max_dd_tolerance: float = 20.0):
        self.min_trades = min_trades
        self.max_dd_tolerance = max_dd_tolerance

    def score(self, metrics: TrialMetrics) -> ObjectiveScore:
        components: Dict[str, float] = {}
        penalties: Dict[str, float] = {}
        rationale_parts = []

        exp_score = (
            metrics.expectancy * 100
            if metrics.expectancy > 0
            else metrics.expectancy * 200
        )
        components[ObjectiveComponent.EXPECTANCY.value] = exp_score
        rationale_parts.append(f"Expectancy base: {exp_score:.2f}")

        pf_score = 0.0
        if metrics.profit_factor > 1.0:
            pf_score = min(metrics.profit_factor - 1.0, 2.0) * 20
        elif metrics.profit_factor > 0:
            pf_score = (metrics.profit_factor - 1.0) * 50
        components[ObjectiveComponent.PROFIT_FACTOR.value] = pf_score

        dd_penalty = 0.0
        if metrics.max_drawdown_pct > self.max_dd_tolerance:
            excess_dd = metrics.max_drawdown_pct - self.max_dd_tolerance
            dd_penalty = -(excess_dd**1.5) * 2
        penalties[ObjectiveComponent.DRAWDOWN_PENALTY.value] = dd_penalty
        if dd_penalty < 0:
            rationale_parts.append(f"DD penalty: {dd_penalty:.2f}")

        tc_penalty = 0.0
        if metrics.total_trades < self.min_trades:
            shortfall = self.min_trades - metrics.total_trades
            tc_penalty = -(shortfall * 10)
        elif metrics.total_trades == 0:
            tc_penalty = -1000
        penalties[ObjectiveComponent.LOW_TRADE_COUNT_PENALTY.value] = tc_penalty
        if tc_penalty < 0:
            rationale_parts.append(f"Low trade count penalty: {tc_penalty:.2f}")

        bm_score = metrics.benchmark_relative_strength * 10
        components[ObjectiveComponent.BENCHMARK_RELATIVE_STRENGTH.value] = bm_score

        total_components = sum(components.values())
        total_penalties = sum(penalties.values())
        total_score = total_components + total_penalties

        rationale = (
            " | ".join(rationale_parts)
            if rationale_parts
            else "Standard composite scoring"
        )

        return ObjectiveScore(
            total_score=total_score,
            component_scores=components,
            penalties=penalties,
            rationale=rationale,
        )
