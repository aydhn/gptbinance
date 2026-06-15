import pytest
from app.reliance_plane.authority import process_authority

def test_process_authority():
    result = process_authority({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "authority"
