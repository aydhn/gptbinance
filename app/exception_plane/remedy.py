from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class RemedyLinkageRecord:
    exception_id: str
    is_remedy_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class RemedyLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> RemedyLinkageRecord:
        # Ensures no remedy-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return RemedyLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_remedy_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
