import pytest
from app.reliance_plane.appeal import process_appeal

def test_process_appeal():
    result = process_appeal({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "appeal"
