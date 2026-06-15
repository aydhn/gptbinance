import pytest
from app.reliance_plane.interpretation import process_interpretation

def test_process_interpretation():
    result = process_interpretation({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "interpretation"
