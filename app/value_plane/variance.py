from typing import Dict, List, Optional
from app.value_plane.models import ValueVarianceRecord

class VarianceRegistry:
    def __init__(self):
        self._records: Dict[str, ValueVarianceRecord] = {}

    def register(self, record: ValueVarianceRecord):
        self._records[record.variance_id] = record

    def get(self, record_id: str) -> Optional[ValueVarianceRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValueVarianceRecord]:
        return list(self._records.values())

variance_registry = VarianceRegistry()
