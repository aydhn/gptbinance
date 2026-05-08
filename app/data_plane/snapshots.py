from typing import Dict, Optional
from .models import DataSnapshot


class SnapshotManager:
    def __init__(self):
        self._snapshots: Dict[str, DataSnapshot] = {}

    def create_snapshot(self, snapshot: DataSnapshot):
        self._snapshots[snapshot.snapshot_id] = snapshot

    def get(self, snapshot_id: str) -> Optional[DataSnapshot]:
        return self._snapshots.get(snapshot_id)

    def list_all(self):
        return list(self._snapshots.values())
