import pytest
from app.reliance_plane.jurisdiction import process_jurisdiction

def test_process_jurisdiction():
    result = process_jurisdiction({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "jurisdiction"
