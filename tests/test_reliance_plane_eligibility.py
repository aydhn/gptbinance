import pytest
from app.reliance_plane.eligibility import process_eligibility

def test_process_eligibility():
    result = process_eligibility({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "eligibility"
