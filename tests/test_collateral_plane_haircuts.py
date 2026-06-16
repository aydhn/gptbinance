import pytest
from app.collateral_plane.haircuts import HaircutsManager

def test_haircuts_registration():
    manager = HaircutsManager()
    entity_id = manager.register_haircuts("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_haircuts(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_haircuts_integrity():
    manager = HaircutsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
