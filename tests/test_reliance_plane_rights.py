import pytest
from app.reliance_plane.rights import process_rights

def test_process_rights():
    result = process_rights({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "rights"
