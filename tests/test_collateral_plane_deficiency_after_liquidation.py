import pytest
from app.collateral_plane.deficiency_after_liquidation import DeficiencyAfterLiquidationManager

def test_deficiency_after_liquidation_registration():
    manager = DeficiencyAfterLiquidationManager()
    entity_id = manager.register_deficiency_after_liquidation("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_deficiency_after_liquidation(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_deficiency_after_liquidation_integrity():
    manager = DeficiencyAfterLiquidationManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
