from app.reviews.models import ReviewHandoff
from app.reviews.enums import HandoffClass
import uuid


class HandoffEngine:
    def handoff(
        self,
        item_id: str,
        handoff_class: HandoffClass,
        from_assignee: str,
        to_assignee: str,
        reason: str,
    ) -> ReviewHandoff:
        return ReviewHandoff(
            handoff_id=str(uuid.uuid4()),
            item_id=item_id,
            handoff_class=handoff_class,
            from_assignee_id=from_assignee,
            to_assignee_id=to_assignee,
            reason=reason,
        )
