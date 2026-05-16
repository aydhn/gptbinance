from typing import Dict, List
from app.program_plane.models import DeliverableRecord

class DeliverableRegistry:
    def __init__(self):
        self._deliverables: Dict[str, DeliverableRecord] = {}

    def register(self, record: DeliverableRecord):
        self._deliverables[record.deliverable_id] = record

    def list_by_milestone(self, milestone_id: str) -> List[DeliverableRecord]:
        return [d for d in self._deliverables.values() if d.milestone_id == milestone_id]
