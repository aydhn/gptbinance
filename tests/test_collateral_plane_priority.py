import pytest
from app.collateral_plane.priority import PriorityManager

def test_priority_registration():
    manager = PriorityManager()
    entity_id = manager.register_priority("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_priority(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_priority_integrity():
    manager = PriorityManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
