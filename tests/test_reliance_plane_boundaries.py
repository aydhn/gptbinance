import pytest
from app.reliance_plane.boundaries import process_boundaries

def test_process_boundaries():
    result = process_boundaries({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "boundaries"
