import pytest
from app.reliance_plane.reliances import process_reliances

def test_process_reliances():
    result = process_reliances({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "reliances"
