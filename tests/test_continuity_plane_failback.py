import pytest
from datetime import datetime, timezone
from app.continuity_plane.failback import FailbackManager
from app.continuity_plane.models import FailbackRecord
from app.continuity_plane.enums import FailbackClass

def test_failback_manager():
    manager = FailbackManager()
    record = FailbackRecord(
        failback_id="fb_1",
        service_id="srv_1",
        failback_class=FailbackClass.PLANNED_RETURN,
        timestamp=datetime.now(timezone.utc),
        is_successful=True,
        actor="admin"
    )
    manager.record_failback(record)

    retrieved = manager.get_failback("fb_1")
    assert retrieved is not None
    assert retrieved.failback_id == "fb_1"
