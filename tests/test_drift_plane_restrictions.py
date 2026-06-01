import pytest
from app.drift_plane.restrictions import RestrictionManager
from app.drift_plane.enums import RestrictionClass

def test_restriction_reimposition_creation():
    manager = RestrictionManager()
    manager.add_restriction("reimposition-1", RestrictionClass.STAGED)

    restriction = manager.get_restriction("reimposition-1")
    assert restriction is not None
    assert restriction.restriction_id == "reimposition-1"
    assert restriction.class_type == RestrictionClass.STAGED
