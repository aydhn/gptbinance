import pytest
from app.reliance_plane.base import process_base

def test_process_base():
    result = process_base({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "base"
