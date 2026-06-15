import pytest
from app.reliance_plane.federation import process_federation

def test_process_federation():
    result = process_federation({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "federation"
