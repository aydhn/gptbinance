import pytest
from app.environment_plane.drift import record_drift

def test_record_drift():
    drift = record_drift("HIGH", "Config drift detected")
    assert drift.severity == "HIGH"
    assert drift.description == "Config drift detected"
