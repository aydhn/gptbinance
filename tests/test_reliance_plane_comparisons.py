import pytest
from app.reliance_plane.comparisons import process_comparisons

def test_process_comparisons():
    result = process_comparisons({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "comparisons"
