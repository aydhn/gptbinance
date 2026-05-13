import pytest
from datetime import datetime, timezone
from app.continuity_plane.standby import StandbyManager
from app.continuity_plane.models import StandbyModeRecord
from app.continuity_plane.enums import StandbyClass

def test_standby_manager():
    manager = StandbyManager()
    record = StandbyModeRecord(
        service_id="srv_1",
        standby_class=StandbyClass.HOT,
        is_fresh=True,
        compatibility_drift=False,
        last_checked=datetime.now(timezone.utc)
    )
    manager.update_standby_mode(record)

    retrieved = manager.get_standby_mode("srv_1")
    assert retrieved is not None
    assert retrieved.service_id == "srv_1"
