import pytest
from app.release_plane.controls import ReleaseControlManager
from app.release_plane.exceptions import ReleasePlaneError

def test_control_action_logging():
    manager = ReleaseControlManager()
    record = manager.log_action("hold", "cand-1", "lin-1")
    assert record.action == "hold"

def test_invalid_control_action():
    manager = ReleaseControlManager()
    with pytest.raises(ReleasePlaneError):
         manager.log_action("hidden_deploy", "cand-1", "lin-1")
