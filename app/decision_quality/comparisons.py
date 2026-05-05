import uuid
from .models import OpportunityOutcome, DecisionComparison
from .enums import DecisionQualityVerdict


class DecisionComparator:
    """
    Compares the outcomes of different decisions within the same context.
    """

    def compare(
        self, base: OpportunityOutcome, target: OpportunityOutcome
    ) -> DecisionComparison:
        """
        Compares two opportunity outcomes to determine relative quality.
        Does not auto-optimize, purely diagnostic.
        """
        verdict = "inconclusive"
        reason = "Comparison inconclusive due to outcome states."

        if base.verdict == DecisionQualityVerdict.EXECUTED_WELL and target.verdict in (
            DecisionQualityVerdict.BLOCKED_AND_LIKELY_SAVED_LOSS,
            DecisionQualityVerdict.INDETERMINATE,
        ):
            verdict = "base_better"
            reason = "Base executed well while target was blocked or indeterminate."
        elif (
            base.verdict == DecisionQualityVerdict.EXECUTED_POORLY
            and target.verdict == DecisionQualityVerdict.BLOCKED_AND_LIKELY_SAVED_LOSS
        ):
            verdict = "target_better"
            reason = "Target blocked a likely loss while base executed poorly."

        return DecisionComparison(
            id=str(uuid.uuid4()),
            base_opportunity_id=base.opportunity_id,
            target_opportunity_id=target.opportunity_id,
            verdict=verdict,
            reason=reason,
        )
