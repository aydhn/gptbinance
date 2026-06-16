import pytest
from app.collateral_plane.concentration import ConcentrationManager

def test_concentration_registration():
    manager = ConcentrationManager()
    entity_id = manager.register_concentration("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_concentration(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_concentration_integrity():
    manager = ConcentrationManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
