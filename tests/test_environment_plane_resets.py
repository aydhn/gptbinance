import pytest
from app.environment_plane.resets import define_reset

def test_define_reset():
    reset = define_reset("Full", "Clean slate")
    assert reset.reset_type == "Full"
    assert reset.drift_notes == "Clean slate"
