from typing import Dict, List, Optional
from app.value_plane.models import OpportunityCostRecord

class OpportunityCostRegistry:
    def __init__(self):
        self._records: Dict[str, OpportunityCostRecord] = {}

    def register(self, record: OpportunityCostRecord):
        self._records[record.record_id] = record

    def get(self, record_id: str) -> Optional[OpportunityCostRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[OpportunityCostRecord]:
        return list(self._records.values())

opportunity_cost_registry = OpportunityCostRegistry()
