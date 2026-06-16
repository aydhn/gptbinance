import pytest
from app.collateral_plane.storage import StorageManager

def test_storage_registration():
    manager = StorageManager()
    entity_id = manager.register_storage("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_storage(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_storage_integrity():
    manager = StorageManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
