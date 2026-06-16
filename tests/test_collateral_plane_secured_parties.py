import pytest
from app.collateral_plane.secured_parties import SecuredPartiesManager

def test_secured_parties_registration():
    manager = SecuredPartiesManager()
    entity_id = manager.register_secured_parties("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_secured_parties(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_secured_parties_integrity():
    manager = SecuredPartiesManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
