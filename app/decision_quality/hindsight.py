from .enums import EvidenceConfidence, HindsightSafetyClass
from typing import List


class HindsightSafeguard:
    """
    Ensures that outcome interpretations do not overclaim due to hindsight bias.
    """

    def evaluate_confidence(
        self,
        is_market_truth_stale: bool,
        is_event_window: bool,
        evidence_refs: List[str],
    ) -> EvidenceConfidence:
        """
        Downgrades confidence based on context conditions like stale data.
        """
        if is_market_truth_stale:
            return EvidenceConfidence.UNSAFE_TO_JUDGE

        if is_event_window:
            return EvidenceConfidence.WEAK

        if not evidence_refs:
            return EvidenceConfidence.MODERATE

        return EvidenceConfidence.STRONG

    def get_safety_class(self, confidence: EvidenceConfidence) -> HindsightSafetyClass:
        """
        Maps confidence to a safety class for reporting.
        """
        if confidence == EvidenceConfidence.UNSAFE_TO_JUDGE:
            return HindsightSafetyClass.UNSAFE
        elif confidence in (EvidenceConfidence.WEAK, EvidenceConfidence.MODERATE):
            return HindsightSafetyClass.CAVEAT_APPLIED
        return HindsightSafetyClass.SAFE
