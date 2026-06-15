import pytest
from app.reliance_plane.consumers import process_consumers

def test_process_consumers():
    result = process_consumers({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "consumers"
