import pytest
from datetime import datetime, timezone
from app.continuity_plane.failover import FailoverManager
from app.continuity_plane.models import FailoverRecord
from app.continuity_plane.enums import FailoverClass

def test_failover_manager():
    manager = FailoverManager()
    record = FailoverRecord(
        failover_id="fo_1",
        service_id="srv_1",
        failover_class=FailoverClass.PLANNED_SWITCHOVER,
        timestamp=datetime.now(timezone.utc),
        is_successful=True,
        actor="admin"
    )
    manager.record_failover(record)

    retrieved = manager.get_failover("fo_1")
    assert retrieved is not None
    assert retrieved.failover_id == "fo_1"
