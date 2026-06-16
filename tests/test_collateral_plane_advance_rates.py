import pytest
from app.collateral_plane.advance_rates import AdvanceRatesManager

def test_advance_rates_registration():
    manager = AdvanceRatesManager()
    entity_id = manager.register_advance_rates("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_advance_rates(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_advance_rates_integrity():
    manager = AdvanceRatesManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
