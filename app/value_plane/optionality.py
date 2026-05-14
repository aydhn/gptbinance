from typing import Dict, List, Optional
from app.value_plane.models import StrategicOptionalityRecord

class OptionalityRegistry:
    def __init__(self):
        self._records: Dict[str, StrategicOptionalityRecord] = {}

    def register(self, record: StrategicOptionalityRecord):
        self._records[record.record_id] = record

    def get(self, record_id: str) -> Optional[StrategicOptionalityRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[StrategicOptionalityRecord]:
        return list(self._records.values())

optionality_registry = OptionalityRegistry()
