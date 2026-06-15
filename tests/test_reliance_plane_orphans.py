import pytest
from app.reliance_plane.orphans import process_orphans

def test_process_orphans():
    result = process_orphans({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "orphans"
