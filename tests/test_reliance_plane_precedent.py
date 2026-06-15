import pytest
from app.reliance_plane.precedent import process_precedent

def test_process_precedent():
    result = process_precedent({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "precedent"
