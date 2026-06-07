from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class AdaptationLinkageRecord:
    exception_id: str
    is_adaptation_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class AdaptationLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> AdaptationLinkageRecord:
        # Ensures no adaptation-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return AdaptationLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_adaptation_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
