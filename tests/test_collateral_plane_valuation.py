import pytest
from app.collateral_plane.valuation import ValuationManager

def test_valuation_registration():
    manager = ValuationManager()
    entity_id = manager.register_valuation("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_valuation(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_valuation_integrity():
    manager = ValuationManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
