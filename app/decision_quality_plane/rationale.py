from typing import List, Dict
from app.decision_quality_plane.models import RationaleRecord
from app.decision_quality_plane.exceptions import HindsightRewriteAttemptError

class RationaleManager:
    def __init__(self):
        self._rationales: Dict[str, List[RationaleRecord]] = {}

    def append_rationale(self, decision_id: str, rationale: RationaleRecord):
        if decision_id not in self._rationales:
            self._rationales[decision_id] = []
        # Append-only check implied by list append
        self._rationales[decision_id].append(rationale)

    def get_latest(self, decision_id: str) -> RationaleRecord:
        if decision_id in self._rationales and self._rationales[decision_id]:
            return self._rationales[decision_id][-1]
        return None

    def get_history(self, decision_id: str) -> List[RationaleRecord]:
        return self._rationales.get(decision_id, [])
