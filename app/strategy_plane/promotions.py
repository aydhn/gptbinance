from app.strategy_plane.enums import LifecycleState, PromotionClass
from app.strategy_plane.exceptions import PromotionError


class StrategyPromotionGovernance:
    def evaluate_promotion(
        self,
        current_state: LifecycleState,
        target_state: LifecycleState,
        evidence_bundle: dict,
    ) -> bool:
        """
        Evaluates if a strategy can be promoted based on provided evidence.
        """
        # Basic state checks
        if (
            current_state == LifecycleState.HYPOTHESIS_ONLY
            and target_state == LifecycleState.RESEARCH_CANDIDATE
        ):
            return self._check_research_evidence(evidence_bundle)

        elif (
            current_state == LifecycleState.REPLAY_QUALIFIED
            and target_state == LifecycleState.PAPER_CANDIDATE
        ):
            return self._check_paper_evidence(evidence_bundle)

        elif (
            current_state == LifecycleState.PAPER_ACTIVE
            and target_state == LifecycleState.PROBATIONARY_LIVE
        ):
            return self._check_probation_evidence(evidence_bundle)

        # ... other transitions ...
        return True  # Fallback for now

    def _check_research_evidence(self, bundle: dict) -> bool:
        if "thesis_ref" not in bundle or "signal_contracts" not in bundle:
            raise PromotionError(
                "Missing thesis or signal contracts for research promotion"
            )
        return True

    def _check_paper_evidence(self, bundle: dict) -> bool:
        if "replay_performance_report" not in bundle:
            raise PromotionError(
                "Missing replay performance report for paper promotion"
            )
        return True

    def _check_probation_evidence(self, bundle: dict) -> bool:
        if (
            "paper_performance_report" not in bundle
            or "equivalence_report" not in bundle
        ):
            raise PromotionError(
                "Missing paper performance or equivalence report for probation promotion"
            )
        return True
