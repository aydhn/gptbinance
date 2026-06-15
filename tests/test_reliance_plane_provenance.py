import pytest
from app.reliance_plane.provenance import process_provenance

def test_process_provenance():
    result = process_provenance({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "provenance"
