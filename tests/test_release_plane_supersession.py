import pytest
from app.release_plane.supersession import SupersessionManager
from app.release_plane.exceptions import RolloutViolation

def test_supersession_recording():
    manager = SupersessionManager()
    record = manager.record_supersession("old-rel", "new-rel", 86400)
    assert record.superseded_release.release_id == "old-rel"
    assert record.superseded_by.release_id == "new-rel"

def test_silent_replacement_rejection():
    manager = SupersessionManager()
    with pytest.raises(RolloutViolation):
         manager.record_supersession("", "new-rel", 86400)
