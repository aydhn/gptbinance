import pytest
from app.reliance_plane.contradictions import process_contradictions

def test_process_contradictions():
    result = process_contradictions({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "contradictions"
