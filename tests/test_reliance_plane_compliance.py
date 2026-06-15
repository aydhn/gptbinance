import pytest
from app.reliance_plane.compliance import process_compliance

def test_process_compliance():
    result = process_compliance({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "compliance"
