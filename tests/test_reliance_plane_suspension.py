import pytest
from app.reliance_plane.suspension import process_suspension

def test_process_suspension():
    result = process_suspension({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "suspension"
