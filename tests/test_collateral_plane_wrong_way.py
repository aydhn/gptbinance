import pytest
from app.collateral_plane.wrong_way import WrongWayManager

def test_wrong_way_registration():
    manager = WrongWayManager()
    entity_id = manager.register_wrong_way("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_wrong_way(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_wrong_way_integrity():
    manager = WrongWayManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
