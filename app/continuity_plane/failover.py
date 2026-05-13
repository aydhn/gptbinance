from typing import Dict, List, Optional
from app.continuity_plane.models import FailoverRecord
from app.continuity_plane.exceptions import FailoverViolation

class FailoverManager:
    def __init__(self):
        self._failovers: Dict[str, FailoverRecord] = {}

    def record_failover(self, record: FailoverRecord) -> None:
        self._failovers[record.failover_id] = record

    def get_failover(self, failover_id: str) -> Optional[FailoverRecord]:
        return self._failovers.get(failover_id)

    def list_failovers(self) -> List[FailoverRecord]:
        return list(self._failovers.values())
