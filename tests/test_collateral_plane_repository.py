import pytest
from app.collateral_plane.repository import RepositoryManager

def test_repository_registration():
    manager = RepositoryManager()
    entity_id = manager.register_repository("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_repository(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_repository_integrity():
    manager = RepositoryManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
