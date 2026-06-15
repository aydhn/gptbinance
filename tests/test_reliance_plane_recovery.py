import pytest
from app.reliance_plane.recovery import process_recovery

def test_process_recovery():
    result = process_recovery({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "recovery"
