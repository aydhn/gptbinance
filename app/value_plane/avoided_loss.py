from typing import Dict, List, Optional
from app.value_plane.models import AvoidedLossRecord

class AvoidedLossRegistry:
    def __init__(self):
        self._records: Dict[str, AvoidedLossRecord] = {}

    def register(self, record: AvoidedLossRecord):
        self._records[record.record_id] = record

    def get(self, record_id: str) -> Optional[AvoidedLossRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[AvoidedLossRecord]:
        return list(self._records.values())

avoided_loss_registry = AvoidedLossRegistry()
