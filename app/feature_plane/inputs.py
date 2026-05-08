# Updated to use Canonical Data Snapshots
from app.data_plane.snapshots import SnapshotManager


class FeatureInputLoader:
    def load_inputs(self, snapshot_id: str, snapshot_manager: SnapshotManager):
        snapshot = snapshot_manager.get(snapshot_id)
        # process snapshot into feature inputs
        return snapshot
