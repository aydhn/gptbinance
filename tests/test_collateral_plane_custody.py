import pytest
from app.collateral_plane.custody import CustodyManager

def test_custody_registration():
    manager = CustodyManager()
    entity_id = manager.register_custody("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_custody(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_custody_integrity():
    manager = CustodyManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
