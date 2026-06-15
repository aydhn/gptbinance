import pytest
from app.reliance_plane.revoked import process_revoked

def test_process_revoked():
    result = process_revoked({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "revoked"
