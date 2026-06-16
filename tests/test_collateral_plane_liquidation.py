import pytest
from app.collateral_plane.liquidation import LiquidationManager

def test_liquidation_registration():
    manager = LiquidationManager()
    entity_id = manager.register_liquidation("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_liquidation(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_liquidation_integrity():
    manager = LiquidationManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
