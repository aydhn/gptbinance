import pytest
from app.collateral_plane.collaterals import CollateralsManager

def test_collaterals_registration():
    manager = CollateralsManager()
    entity_id = manager.register_collaterals("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_collaterals(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_collaterals_integrity():
    manager = CollateralsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
