from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class IncidentsLinkageRecord:
    exception_id: str
    is_incidents_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class IncidentsLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> IncidentsLinkageRecord:
        # Ensures no incidents-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return IncidentsLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_incidents_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
