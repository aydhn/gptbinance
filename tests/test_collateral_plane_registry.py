import pytest
from app.collateral_plane.registry import RegistryManager

def test_registry_registration():
    manager = RegistryManager()
    entity_id = manager.register_registry("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_registry(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_registry_integrity():
    manager = RegistryManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
