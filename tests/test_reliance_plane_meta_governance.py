import pytest
from app.reliance_plane.meta_governance import process_meta_governance

def test_process_meta_governance():
    result = process_meta_governance({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "meta_governance"
