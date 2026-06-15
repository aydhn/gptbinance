import pytest
from app.reliance_plane.revocation import process_revocation

def test_process_revocation():
    result = process_revocation({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "revocation"
