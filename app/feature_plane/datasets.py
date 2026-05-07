from typing import Dict, Optional
from app.feature_plane.models import DatasetSnapshot


class DatasetSnapshotManager:
    def __init__(self):
        self._snapshots: Dict[str, DatasetSnapshot] = {}

    def store(self, snapshot: DatasetSnapshot) -> None:
        self._snapshots[snapshot.snapshot_id] = snapshot

    def get(self, snapshot_id: str) -> Optional[DatasetSnapshot]:
        return self._snapshots.get(snapshot_id)
