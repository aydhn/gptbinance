from typing import Dict, List, Optional
from app.federation_plane.models import FederationRecord


class FederationManager:
    def __init__(self):
        self._records: Dict[str, FederationRecord] = {}

    def register(self, record: FederationRecord):
        self._records[record.federation_id] = record

    def get_record(self, federation_id: str) -> Optional[FederationRecord]:
        return self._records.get(federation_id)

    def list_records(self) -> List[FederationRecord]:
        return list(self._records.values())
