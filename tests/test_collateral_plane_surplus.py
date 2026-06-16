import pytest
from app.collateral_plane.surplus import SurplusManager

def test_surplus_registration():
    manager = SurplusManager()
    entity_id = manager.register_surplus("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_surplus(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_surplus_integrity():
    manager = SurplusManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
