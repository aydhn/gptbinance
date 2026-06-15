import pytest
from app.reliance_plane.incidents import process_incidents

def test_process_incidents():
    result = process_incidents({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "incidents"
