import pytest
from app.reliance_plane.denials import process_denials

def test_process_denials():
    result = process_denials({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "denials"
