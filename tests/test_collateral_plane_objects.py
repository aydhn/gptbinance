import pytest
from app.collateral_plane.objects import ObjectsManager

def test_objects_registration():
    manager = ObjectsManager()
    entity_id = manager.register_objects("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_objects(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_objects_integrity():
    manager = ObjectsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
