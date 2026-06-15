import pytest
from app.reliance_plane.overreliance import process_overreliance

def test_process_overreliance():
    result = process_overreliance({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "overreliance"
