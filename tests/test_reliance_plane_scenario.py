import pytest
from app.reliance_plane.scenario import process_scenario

def test_process_scenario():
    result = process_scenario({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "scenario"
