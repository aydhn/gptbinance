import pytest
from app.reliance_plane.readiness import process_readiness

def test_process_readiness():
    result = process_readiness({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "readiness"
