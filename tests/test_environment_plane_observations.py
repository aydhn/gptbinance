import pytest
from app.environment_plane.observations import record_observation

def test_record_observation():
    obs = record_observation("ParityCheck", "Verified visually")
    assert obs.observation_type == "ParityCheck"
    assert obs.sufficiency_notes == "Verified visually"
