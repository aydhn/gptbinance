import pytest
from app.reliance_plane.misreliance import process_misreliance

def test_process_misreliance():
    result = process_misreliance({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "misreliance"
