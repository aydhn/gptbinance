import pytest
from app.collateral_plane.release import ReleaseManager

def test_release_registration():
    manager = ReleaseManager()
    entity_id = manager.register_release("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_release(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_release_integrity():
    manager = ReleaseManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
