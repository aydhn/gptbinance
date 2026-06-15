import pytest
from app.reliance_plane.immunity import process_immunity

def test_process_immunity():
    result = process_immunity({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "immunity"
