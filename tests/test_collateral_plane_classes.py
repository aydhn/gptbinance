import pytest
from app.collateral_plane.classes import ClassesManager

def test_classes_registration():
    manager = ClassesManager()
    entity_id = manager.register_classes("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_classes(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_classes_integrity():
    manager = ClassesManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
