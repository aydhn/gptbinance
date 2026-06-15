import pytest
from app.reliance_plane.validity import process_validity

def test_process_validity():
    result = process_validity({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "validity"
