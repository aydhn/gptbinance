import pytest
from app.reliance_plane.provisional import process_provisional

def test_process_provisional():
    result = process_provisional({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "provisional"
