from app.program_plane.models import EscalationRecord
from app.program_plane.enums import EscalationClass

class EscalationManager:
    def escalate(self, program_id: str) -> EscalationRecord:
        return EscalationRecord(
            escalation_id=f"esc_{program_id}",
            program_id=program_id,
            escalation_class=EscalationClass.BLOCKER
        )
