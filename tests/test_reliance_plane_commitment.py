import pytest
from app.reliance_plane.commitment import process_commitment

def test_process_commitment():
    result = process_commitment({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "commitment"
