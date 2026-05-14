from typing import Dict, List, Optional
from app.value_plane.models import CostOfDelayRecord

class CostOfDelayRegistry:
    def __init__(self):
        self._records: Dict[str, CostOfDelayRecord] = {}

    def register(self, record: CostOfDelayRecord):
        self._records[record.record_id] = record

    def get(self, record_id: str) -> Optional[CostOfDelayRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[CostOfDelayRecord]:
        return list(self._records.values())

cost_of_delay_registry = CostOfDelayRegistry()
