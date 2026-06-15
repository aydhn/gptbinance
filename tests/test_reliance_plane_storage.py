import pytest
from app.reliance_plane.storage import process_storage

def test_process_storage():
    result = process_storage({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "storage"
