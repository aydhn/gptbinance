import pytest
from app.environment_plane.rot import record_rot

def test_record_rot():
    rot = record_rot("Stale DR", "MEDIUM")
    assert rot.rot_description == "Stale DR"
    assert rot.severity == "MEDIUM"
