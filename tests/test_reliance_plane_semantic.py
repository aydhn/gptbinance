import pytest
from app.reliance_plane.semantic import process_semantic

def test_process_semantic():
    result = process_semantic({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "semantic"
