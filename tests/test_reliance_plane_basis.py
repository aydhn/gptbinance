import pytest
from app.reliance_plane.basis import process_basis

def test_process_basis():
    result = process_basis({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "basis"
