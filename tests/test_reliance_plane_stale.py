import pytest
from app.reliance_plane.stale import process_stale

def test_process_stale():
    result = process_stale({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "stale"
