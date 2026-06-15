import pytest
from app.reliance_plane.remedy import process_remedy

def test_process_remedy():
    result = process_remedy({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "remedy"
