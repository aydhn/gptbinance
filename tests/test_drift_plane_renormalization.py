import pytest
from app.drift_plane.renormalization import RenormalizationManager
from app.drift_plane.enums import RenormalizationClass

def test_renormalization_prerequisite_creation():
    manager = RenormalizationManager()
    manager.add_prerequisite("prereq-1", RenormalizationClass.REQUIRED_RE_BASELINING)

    prereq = manager.get_prerequisite("prereq-1")
    assert prereq is not None
    assert prereq.prereq_id == "prereq-1"
    assert prereq.class_type == RenormalizationClass.REQUIRED_RE_BASELINING
    assert prereq.satisfied is False
