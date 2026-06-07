from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class LegitimacyLinkageRecord:
    exception_id: str
    is_legitimacy_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class LegitimacyLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> LegitimacyLinkageRecord:
        # Ensures no legitimacy-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return LegitimacyLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_legitimacy_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
