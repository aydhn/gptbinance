import pytest
from app.collateral_plane.possession import PossessionManager

def test_possession_registration():
    manager = PossessionManager()
    entity_id = manager.register_possession("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_possession(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_possession_integrity():
    manager = PossessionManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
