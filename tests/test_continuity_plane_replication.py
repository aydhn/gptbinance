import pytest
from app.continuity_plane.replication import ReplicationManager
from app.continuity_plane.models import ReplicationRecord
from app.continuity_plane.enums import ReplicationClass

def test_replication_manager():
    manager = ReplicationManager()
    record = ReplicationRecord(
        replication_id="repl_1",
        service_id="srv_1",
        replication_class=ReplicationClass.SYNC,
        lag_seconds=0,
        is_healthy=True,
        lineage_ref="ref_123"
    )
    manager.record_replication(record)

    retrieved = manager.get_replication("repl_1")
    assert retrieved is not None
    assert retrieved.replication_id == "repl_1"
