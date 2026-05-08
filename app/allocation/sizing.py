from app.allocation.models import AllocationCandidate, AllocationIntent
from app.allocation.enums import AllocationVerdict


class SizingEngine:
    def __init__(self):
        self.min_viable_size = 10.0  # Example

    def determine_size(
        self, candidate: AllocationCandidate, available_headroom: float
    ) -> AllocationIntent:
        base_size = candidate.requested_notional * candidate.confidence
        clipped_size = base_size
        clip_reasons = []
        verdict = AllocationVerdict.ACCEPTED

        if clipped_size > available_headroom:
            clipped_size = available_headroom
            clip_reasons.append("budget_headroom_clip")
            verdict = AllocationVerdict.CLIPPED

        reject_reason = None
        if clipped_size < self.min_viable_size:
            verdict = AllocationVerdict.REJECTED
            reject_reason = "below_min_viable_size"
            clipped_size = 0.0

        return AllocationIntent(
            intent_id=f"intent_{candidate.candidate_id}",
            candidate_id=candidate.candidate_id,
            symbol=candidate.symbol,
            sleeve_ref=candidate.sleeve_ref,
            verdict=verdict,
            base_size=base_size,
            clipped_size=clipped_size,
            clip_reasons=clip_reasons,
            reject_reason=reject_reason,
            budget_ref=f"budget_{candidate.sleeve_ref}",
            route_ref=f"route_{candidate.sleeve_ref}",
        )
