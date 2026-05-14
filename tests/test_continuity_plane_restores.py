import pytest
from datetime import datetime, timezone
from app.continuity_plane.restores import RestoreManager
from app.continuity_plane.models import RestoreRecord
from app.continuity_plane.enums import RestoreClass

def test_restore_manager():
    manager = RestoreManager()
    record = RestoreRecord(
        restore_id="rest_1",
        service_id="srv_1",
        snapshot_id="snap_1",
        restore_class=RestoreClass.FULL_RESTORE,
        timestamp=datetime.now(timezone.utc),
        is_successful=True,
        actor="admin"
    )
    manager.record_restore(record)

    retrieved = manager.get_restore("rest_1")
    assert retrieved is not None
    assert retrieved.restore_id == "rest_1"
