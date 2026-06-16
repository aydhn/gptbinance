import pytest
from app.collateral_plane.encumbrances import EncumbrancesManager

def test_encumbrances_registration():
    manager = EncumbrancesManager()
    entity_id = manager.register_encumbrances("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_encumbrances(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_encumbrances_integrity():
    manager = EncumbrancesManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
