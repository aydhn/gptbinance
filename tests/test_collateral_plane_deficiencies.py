import pytest
from app.collateral_plane.deficiencies import DeficienciesManager

def test_deficiencies_registration():
    manager = DeficienciesManager()
    entity_id = manager.register_deficiencies("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_deficiencies(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_deficiencies_integrity():
    manager = DeficienciesManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
