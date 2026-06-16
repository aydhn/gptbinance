import pytest
from app.collateral_plane.closeout import CloseoutManager

def test_closeout_registration():
    manager = CloseoutManager()
    entity_id = manager.register_closeout("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_closeout(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_closeout_integrity():
    manager = CloseoutManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
