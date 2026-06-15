import pytest
from app.reliance_plane.debt import process_debt

def test_process_debt():
    result = process_debt({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "debt"
