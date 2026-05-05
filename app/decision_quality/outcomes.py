from typing import List
from .models import OpportunityOutcome, DecisionOutcomeWindow, DecisionQualityVerdict
from .enums import EvidenceConfidence
from .hindsight import HindsightSafeguard


class OutcomeEvaluator:
    """
    Evaluates the outcome of an opportunity within a given window.
    """

    def __init__(self):
        self.safeguard = HindsightSafeguard()

    def evaluate_executed(
        self,
        opportunity_id: str,
        window: DecisionOutcomeWindow,
        realized_pnl: float,
        is_stale: bool,
        is_event: bool,
        evidence: List[str],
    ) -> OpportunityOutcome:
        """
        Evaluates the outcome of an executed decision.
        """
        confidence = self.safeguard.evaluate_confidence(is_stale, is_event, evidence)

        verdict = DecisionQualityVerdict.INDETERMINATE
        if confidence != EvidenceConfidence.UNSAFE_TO_JUDGE:
            if realized_pnl > 0:
                verdict = DecisionQualityVerdict.EXECUTED_WELL
            elif realized_pnl < 0:
                verdict = DecisionQualityVerdict.EXECUTED_POORLY

        return OpportunityOutcome(
            opportunity_id=opportunity_id,
            window=window,
            realized_pnl=realized_pnl,
            confidence=confidence,
            verdict=verdict,
            evidence_refs=evidence,
        )

    def evaluate_blocked(
        self,
        opportunity_id: str,
        window: DecisionOutcomeWindow,
        simulated_pnl: float,
        is_stale: bool,
        is_event: bool,
        evidence: List[str],
    ) -> OpportunityOutcome:
        """
        Evaluates the simulated outcome of a blocked decision (cautiously).
        """
        confidence = self.safeguard.evaluate_confidence(is_stale, is_event, evidence)

        verdict = DecisionQualityVerdict.INDETERMINATE
        if confidence != EvidenceConfidence.UNSAFE_TO_JUDGE:
            if simulated_pnl < 0:
                verdict = DecisionQualityVerdict.BLOCKED_AND_LIKELY_SAVED_LOSS
            elif simulated_pnl > 0:
                # Cautious interpretation
                verdict = DecisionQualityVerdict.MISSED_ALPHA_CANDIDATE

        return OpportunityOutcome(
            opportunity_id=opportunity_id,
            window=window,
            max_favorable_excursion=simulated_pnl if simulated_pnl > 0 else 0,
            max_adverse_excursion=abs(simulated_pnl) if simulated_pnl < 0 else 0,
            confidence=confidence,
            verdict=verdict,
            evidence_refs=evidence,
        )
