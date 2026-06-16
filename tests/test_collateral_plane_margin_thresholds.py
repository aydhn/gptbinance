import pytest
from app.collateral_plane.margin_thresholds import MarginThresholdsManager

def test_margin_thresholds_registration():
    manager = MarginThresholdsManager()
    entity_id = manager.register_margin_thresholds("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_margin_thresholds(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_margin_thresholds_integrity():
    manager = MarginThresholdsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
