import pytest
from app.reliance_plane.legitimacy import process_legitimacy

def test_process_legitimacy():
    result = process_legitimacy({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "legitimacy"
