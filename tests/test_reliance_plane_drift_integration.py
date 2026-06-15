import pytest
from app.reliance_plane.drift_integration import process_drift_integration

def test_process_drift_integration():
    result = process_drift_integration({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "drift_integration"
