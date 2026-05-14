from typing import Dict, List, Optional
from app.value_plane.models import NegativeExternalityRecord

class ExternalityRegistry:
    def __init__(self):
        self._records: Dict[str, NegativeExternalityRecord] = {}

    def register(self, record: NegativeExternalityRecord):
        self._records[record.externality_id] = record

    def get(self, record_id: str) -> Optional[NegativeExternalityRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[NegativeExternalityRecord]:
        return list(self._records.values())

externality_registry = ExternalityRegistry()
