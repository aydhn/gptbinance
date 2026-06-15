import pytest
from app.reliance_plane.counterparty import process_counterparty

def test_process_counterparty():
    result = process_counterparty({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "counterparty"
