import pytest
from app.release_plane.holds import HoldManager
from app.release_plane.exceptions import RolloutViolation

def test_hold_lifecycle():
    manager = HoldManager()
    hold = manager.apply_hold("c-1", "approval_hold", 3600, "Waiting for signoff")

    manager.release_hold(hold.hold_id, "user1", "Approved via slack")
    assert hold.hold_id not in manager._holds

def test_hold_expired():
    manager = HoldManager()
    hold = manager.apply_hold("c-1", "approval_hold", -1, "Waiting for signoff") # Instantly expired

    with pytest.raises(RolloutViolation):
         manager.release_hold(hold.hold_id, "user1", "Approved")
