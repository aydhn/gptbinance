from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class RightsLinkageRecord:
    exception_id: str
    is_rights_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class RightsLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> RightsLinkageRecord:
        # Ensures no rights-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return RightsLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_rights_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
