import pytest
from app.collateral_plane.manifests import ManifestsManager

def test_manifests_registration():
    manager = ManifestsManager()
    entity_id = manager.register_manifests("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_manifests(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_manifests_integrity():
    manager = ManifestsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
