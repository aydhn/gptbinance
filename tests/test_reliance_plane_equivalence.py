import pytest
from app.reliance_plane.equivalence import process_equivalence

def test_process_equivalence():
    result = process_equivalence({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "equivalence"
