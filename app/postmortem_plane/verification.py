from datetime import datetime
from app.postmortem_plane.models import ActionVerificationRecord
from app.postmortem_plane.enums import VerificationClass, EffectivenessClass
from app.postmortem_plane.exceptions import VerificationViolationError

class ActionVerifier:
    @staticmethod
    def verify(v_id: str, v_class: VerificationClass, notes: str, effectiveness: EffectivenessClass = None, by: str = None) -> ActionVerificationRecord:
        if v_class in [VerificationClass.EFFECTIVENESS, VerificationClass.NO_REGRESSION] and not effectiveness:
             raise VerificationViolationError("Effectiveness must be specified for effectiveness verifications")

        return ActionVerificationRecord(
            verification_id=v_id,
            verification_class=v_class,
            effectiveness=effectiveness,
            proof_notes=notes,
            verified_at=datetime.now(),
            verified_by=by
        )
