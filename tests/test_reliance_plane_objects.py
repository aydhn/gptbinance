import pytest
from app.reliance_plane.objects import process_objects

def test_process_objects():
    result = process_objects({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "objects"
