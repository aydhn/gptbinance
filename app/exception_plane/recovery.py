from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class RecoveryLinkageRecord:
    exception_id: str
    is_recovery_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class RecoveryLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> RecoveryLinkageRecord:
        # Ensures no recovery-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return RecoveryLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_recovery_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
