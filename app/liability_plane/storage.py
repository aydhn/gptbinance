from typing import Dict
from app.liability_plane.models import LiabilityRecord

class LiabilityStorage:
    def __init__(self):
        self._store: Dict[str, LiabilityRecord] = {}

    def save(self, record: LiabilityRecord):
        self._store[record.liability.liability_id] = record

    def load(self, liability_id: str) -> LiabilityRecord:
        return self._store.get(liability_id)

    def get_all(self):
        return list(self._store.values())
