import pytest
from app.reliance_plane.liability import process_liability

def test_process_liability():
    result = process_liability({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "liability"
