import pytest
from app.collateral_plane.call_deadlines import CallDeadlinesManager

def test_call_deadlines_registration():
    manager = CallDeadlinesManager()
    entity_id = manager.register_call_deadlines("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_call_deadlines(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_call_deadlines_integrity():
    manager = CallDeadlinesManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
