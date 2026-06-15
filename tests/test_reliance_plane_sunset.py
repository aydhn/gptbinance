import pytest
from app.reliance_plane.sunset import process_sunset

def test_process_sunset():
    result = process_sunset({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "sunset"
