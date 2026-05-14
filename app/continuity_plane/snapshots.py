from typing import Dict, List, Optional
from app.continuity_plane.models import SnapshotRecord
from app.continuity_plane.exceptions import InvalidSnapshotRecord

class SnapshotManager:
    def __init__(self):
        self._snapshots: Dict[str, SnapshotRecord] = {}

    def record_snapshot(self, snapshot: SnapshotRecord) -> None:
        if not snapshot.snapshot_id or not snapshot.service_id:
            raise InvalidSnapshotRecord("snapshot_id and service_id must be provided")
        self._snapshots[snapshot.snapshot_id] = snapshot

    def get_snapshot(self, snapshot_id: str) -> Optional[SnapshotRecord]:
        return self._snapshots.get(snapshot_id)

    def list_snapshots(self) -> List[SnapshotRecord]:
        return list(self._snapshots.values())
