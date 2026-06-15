import pytest
from app.reliance_plane.contracts import process_contracts

def test_process_contracts():
    result = process_contracts({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "contracts"
