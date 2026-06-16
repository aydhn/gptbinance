import pytest
from app.collateral_plane.liquidation_triggers import LiquidationTriggersManager

def test_liquidation_triggers_registration():
    manager = LiquidationTriggersManager()
    entity_id = manager.register_liquidation_triggers("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_liquidation_triggers(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_liquidation_triggers_integrity():
    manager = LiquidationTriggersManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
