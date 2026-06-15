import pytest
from app.reliance_plane.investigation import process_investigation

def test_process_investigation():
    result = process_investigation({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "investigation"
