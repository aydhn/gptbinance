import pytest
from app.reliance_plane.reporting import process_reporting

def test_process_reporting():
    result = process_reporting({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "reporting"
