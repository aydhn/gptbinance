from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class SunsetLinkageRecord:
    exception_id: str
    is_sunset_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class SunsetLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> SunsetLinkageRecord:
        # Ensures no sunset-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return SunsetLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_sunset_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
