from app.strategy_plane.models import (
    StrategyTrustVerdict,
    StrategyDefinition,
    StrategyEquivalenceReport,
    StrategyDecayReport,
    StrategyOverlapReport,
)
from app.strategy_plane.enums import (
    TrustVerdict,
    EquivalenceVerdict,
    DecaySeverity,
    LifecycleState,
)
from app.strategy_plane.lifecycle import StrategyLifecycleEvaluator


class StrategyTrustEvaluator:
    def evaluate(
        self,
        strategy: StrategyDefinition,
        lifecycle_state: LifecycleState,
        equivalence_report: StrategyEquivalenceReport = None,
        decay_report: StrategyDecayReport = None,
        overlap_report: StrategyOverlapReport = None,
    ) -> StrategyTrustVerdict:
        factors = {}
        verdict = TrustVerdict.TRUSTED

        if lifecycle_state in [LifecycleState.RETIRED, LifecycleState.ARCHIVED]:
            verdict = TrustVerdict.BLOCKED
            factors["lifecycle"] = f"Strategy is {lifecycle_state.name}"

        if lifecycle_state == LifecycleState.FROZEN:
            verdict = TrustVerdict.BLOCKED
            factors["lifecycle"] = "Strategy is frozen"

        if lifecycle_state == LifecycleState.DEGRADED:
            verdict = min(
                verdict, TrustVerdict.DEGRADED
            )  # Enum logic simplification, assume ordering
            verdict = TrustVerdict.DEGRADED
            factors["lifecycle"] = "Strategy is degraded"

        if (
            equivalence_report
            and equivalence_report.verdict == EquivalenceVerdict.DIVERGENT
        ):
            verdict = TrustVerdict.BLOCKED
            factors["equivalence"] = "Strategy is divergent across environments"

        if decay_report and decay_report.severity in [
            DecaySeverity.CRITICAL,
            DecaySeverity.HIGH,
        ]:
            verdict = TrustVerdict.DEGRADED
            factors["decay"] = f"Strategy has {decay_report.severity.name} decay"

        if overlap_report and overlap_report.severity == "CRITICAL":
            if verdict == TrustVerdict.TRUSTED:
                verdict = TrustVerdict.REVIEW_REQUIRED
            factors[
                "overlap"
            ] = "Strategy has critical overlap with other active strategies"

        # Minimum thesis requirements
        if not strategy.thesis_ref or not strategy.hypothesis_ref:
            verdict = TrustVerdict.BLOCKED
            factors["thesis"] = "Missing hypothesis or thesis reference"

        return StrategyTrustVerdict(
            strategy_id=strategy.strategy_id, verdict=verdict, factors=factors
        )
