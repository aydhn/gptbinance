import pytest
from app.reliance_plane.autonomy import process_autonomy

def test_process_autonomy():
    result = process_autonomy({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "autonomy"
