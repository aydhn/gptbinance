import pytest
from datetime import datetime, timezone
from app.continuity_plane.snapshots import SnapshotManager
from app.continuity_plane.models import SnapshotRecord
from app.continuity_plane.enums import SnapshotClass
from app.continuity_plane.exceptions import InvalidSnapshotRecord

def test_snapshot_manager():
    manager = SnapshotManager()
    record = SnapshotRecord(
        snapshot_id="snap_1",
        service_id="srv_1",
        snapshot_class=SnapshotClass.POINT_IN_TIME,
        timestamp=datetime.now(timezone.utc),
        is_complete=True,
        is_stale=False,
        lineage_ref="ref_123"
    )
    manager.record_snapshot(record)

    retrieved = manager.get_snapshot("snap_1")
    assert retrieved is not None
    assert retrieved.snapshot_id == "snap_1"

def test_snapshot_manager_invalid():
    manager = SnapshotManager()
    with pytest.raises(InvalidSnapshotRecord):
        record = SnapshotRecord(
            snapshot_id="",
            service_id="srv_1",
            snapshot_class=SnapshotClass.POINT_IN_TIME,
            timestamp=datetime.now(timezone.utc),
            is_complete=True,
            is_stale=False,
            lineage_ref="ref_123"
        )
        manager.record_snapshot(record)
