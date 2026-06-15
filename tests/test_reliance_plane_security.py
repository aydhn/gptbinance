import pytest
from app.reliance_plane.security import process_security

def test_process_security():
    result = process_security({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "security"
