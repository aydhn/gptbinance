from app.research_plane.models import ResearchInvalidationRecord, ResearchItem
from app.research_plane.enums import InvalidationClass, ConfidenceClass


class InvalidationManager:
    def invalidate(
        self, item: ResearchItem, reason: str, inv_class: InvalidationClass
    ) -> None:
        record = ResearchInvalidationRecord(
            hypothesis_ref=(
                item.hypotheses[0].hypothesis_id if item.hypotheses else "unknown"
            ),
            invalidation_class=inv_class,
            reason=reason,
        )
        item.invalidation = record
        if item.confidence:
            item.confidence.previous_class = item.confidence.current_class
            item.confidence.current_class = ConfidenceClass.INVALIDATED
            item.confidence.transition_reason = f"Invalidated: {reason}"
