import pytest
from app.reliance_plane.scopes import process_scopes

def test_process_scopes():
    result = process_scopes({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "scopes"
