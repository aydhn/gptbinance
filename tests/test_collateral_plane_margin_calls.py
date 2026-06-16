import pytest
from app.collateral_plane.margin_calls import MarginCallsManager

def test_margin_calls_registration():
    manager = MarginCallsManager()
    entity_id = manager.register_margin_calls("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_margin_calls(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_margin_calls_integrity():
    manager = MarginCallsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
