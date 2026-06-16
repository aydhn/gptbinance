import pytest
from app.collateral_plane.obligations import ObligationsManager

def test_obligations_registration():
    manager = ObligationsManager()
    entity_id = manager.register_obligations("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_obligations(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_obligations_integrity():
    manager = ObligationsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
