import pytest
from app.reliance_plane.normalization import process_normalization

def test_process_normalization():
    result = process_normalization({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "normalization"
