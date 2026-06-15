import pytest
from app.reliance_plane.decision_use import process_decision_use

def test_process_decision_use():
    result = process_decision_use({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "decision_use"
