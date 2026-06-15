import pytest
from app.reliance_plane.quality import process_quality

def test_process_quality():
    result = process_quality({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "quality"
