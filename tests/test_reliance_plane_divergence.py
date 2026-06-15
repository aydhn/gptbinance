import pytest
from app.reliance_plane.divergence import process_divergence

def test_process_divergence():
    result = process_divergence({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "divergence"
