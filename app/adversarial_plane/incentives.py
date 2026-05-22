from typing import List, Optional
from app.adversarial_plane.models import IncentiveRecord
from app.adversarial_plane.enums import IncentiveClass

def create_incentive(incentive_id: str, incentive_class: IncentiveClass, ambiguity_notes: str, lineage_refs: Optional[List[str]] = None) -> IncentiveRecord:
    return IncentiveRecord(
        incentive_id=incentive_id,
        incentive_class=incentive_class,
        ambiguity_notes=ambiguity_notes,
        lineage_refs=lineage_refs or []
    )

class IncentiveManager:
    def __init__(self):
        self._incentives = {}

    def add_incentive(self, inc: IncentiveRecord):
        self._incentives[inc.incentive_id] = inc

    def get_incentive(self, incentive_id: str) -> Optional[IncentiveRecord]:
        return self._incentives.get(incentive_id)

    def list_incentives(self) -> List[IncentiveRecord]:
        return list(self._incentives.values())
