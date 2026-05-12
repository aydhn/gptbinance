from datetime import datetime
from typing import Dict, List, Optional

from .enums import ReliabilityStateClass
from .models import ReliabilityStateSnapshot


class StateManager:
    def __init__(self):
        self._snapshots: Dict[str, List[ReliabilityStateSnapshot]] = {}

    def record_state(self, snapshot: ReliabilityStateSnapshot) -> None:
        if snapshot.service_id not in self._snapshots:
            self._snapshots[snapshot.service_id] = []
        self._snapshots[snapshot.service_id].append(snapshot)

    def get_current_state(self, service_id: str) -> Optional[ReliabilityStateSnapshot]:
        snapshots = self._snapshots.get(service_id, [])
        if not snapshots:
            return None
        return sorted(snapshots, key=lambda s: s.timestamp)[-1]

    def list_state_history(self, service_id: str) -> List[ReliabilityStateSnapshot]:
        return sorted(self._snapshots.get(service_id, []), key=lambda s: s.timestamp)
