import pytest
from app.reliance_plane.tradeoff import process_tradeoff

def test_process_tradeoff():
    result = process_tradeoff({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "tradeoff"
