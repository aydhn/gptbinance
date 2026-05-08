from app.execution_plane.models import ExecutionCandidate
from app.execution_plane.base import CandidateCompilerBase
from app.execution_plane.venues import VenueRegistry
from typing import Any


class AllocationIntentCompiler(CandidateCompilerBase):
    """Compiles an Allocation Intent into an Execution Candidate."""

    def __init__(self, venue_registry: VenueRegistry):
        self.venue_registry = venue_registry

    def compile(self, intent: Any) -> ExecutionCandidate:
        # Assuming intent has attributes: intent_id, symbol, target_size, direction, is_reduce_only, venue_class_preference

        candidate = ExecutionCandidate(
            allocation_intent_id=getattr(intent, "intent_id", "unknown"),
            symbol=getattr(intent, "symbol", "UNKNOWN"),
            target_size=getattr(intent, "target_size", 0.0),
            side="buy" if getattr(intent, "direction", "long") == "long" else "sell",
            is_reduce_only=getattr(intent, "is_reduce_only", False),
            venue_eligibility=[],
            instrument_compatibility=True,
            size_viable=True,
        )

        pref = getattr(intent, "venue_class_preference", "paper")
        for v in self.venue_registry.list_venues():
            if v.venue_class.value == pref:
                candidate.venue_eligibility.append(v.venue_id)

        if not candidate.venue_eligibility:
            candidate.reject_reason = "No eligible venues found for preference."
            candidate.size_viable = False

        if candidate.target_size <= 0:
            candidate.reject_reason = "Target size is zero or negative."
            candidate.size_viable = False

        return candidate
