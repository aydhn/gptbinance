import pytest
from datetime import datetime, timezone
from app.continuity_plane.states import ContinuityStateManager
from app.continuity_plane.models import ContinuityStateSnapshot

def test_state_manager():
    manager = ContinuityStateManager()
    record = ContinuityStateSnapshot(
        service_id="srv_1",
        state="protected",
        timestamp=datetime.now(timezone.utc)
    )
    manager.update_state(record)

    retrieved = manager.get_state("srv_1")
    assert retrieved is not None
    assert retrieved.service_id == "srv_1"
