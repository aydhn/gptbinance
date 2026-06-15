import pytest
from app.reliance_plane.oversight import process_oversight

def test_process_oversight():
    result = process_oversight({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "oversight"
