import pytest
from app.reliance_plane.accountability import process_accountability

def test_process_accountability():
    result = process_accountability({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "accountability"
