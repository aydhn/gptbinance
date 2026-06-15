import pytest
from app.reliance_plane.assurance import process_assurance

def test_process_assurance():
    result = process_assurance({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "assurance"
