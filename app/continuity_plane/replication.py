from typing import Dict, List, Optional
from app.continuity_plane.models import ReplicationRecord

class ReplicationManager:
    def __init__(self):
        self._records: Dict[str, ReplicationRecord] = {}

    def record_replication(self, record: ReplicationRecord) -> None:
        self._records[record.replication_id] = record

    def get_replication(self, replication_id: str) -> Optional[ReplicationRecord]:
        return self._records.get(replication_id)

    def list_replications(self) -> List[ReplicationRecord]:
        return list(self._records.values())
