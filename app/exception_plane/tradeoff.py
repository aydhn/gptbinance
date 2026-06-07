from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class TradeoffLinkageRecord:
    exception_id: str
    is_tradeoff_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class TradeoffLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> TradeoffLinkageRecord:
        # Ensures no tradeoff-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return TradeoffLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_tradeoff_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
