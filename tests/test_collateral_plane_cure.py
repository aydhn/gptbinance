import pytest
from app.collateral_plane.cure import CureManager

def test_cure_registration():
    manager = CureManager()
    entity_id = manager.register_cure("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_cure(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_cure_integrity():
    manager = CureManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
