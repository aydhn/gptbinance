from app.reviews.models import ReviewEscalation
from app.reviews.enums import EscalationClass
from app.reviews.exceptions import EscalationError
from app.reviews.base import EscalationEngineBase
import uuid


class EscalationEngine(EscalationEngineBase):
    def escalate(
        self,
        item_id: str,
        escalation_class: EscalationClass,
        reason: str,
        escalated_by: str,
        escalated_to_role: str,
    ) -> ReviewEscalation:
        if not reason:
            raise EscalationError("Escalation requires a reason.")

        return ReviewEscalation(
            escalation_id=str(uuid.uuid4()),
            item_id=item_id,
            escalation_class=escalation_class,
            reason=reason,
            escalated_by=escalated_by,
            escalated_to_role=escalated_to_role,
        )
