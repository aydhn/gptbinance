from typing import Dict, List
from app.program_plane.models import AcceptanceRecord

class AcceptanceManager:
    def __init__(self):
        self._acceptances: Dict[str, AcceptanceRecord] = {}

    def record_acceptance(self, record: AcceptanceRecord):
        self._acceptances[record.acceptance_id] = record

    def is_accepted(self, deliverable_id: str) -> bool:
        return any(a.deliverable_id == deliverable_id and a.state == "accepted" for a in self._acceptances.values())
