import pytest
from app.reliance_plane.constitution import process_constitution

def test_process_constitution():
    result = process_constitution({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "constitution"
