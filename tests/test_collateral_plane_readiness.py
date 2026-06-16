import pytest
from app.collateral_plane.readiness import ReadinessManager

def test_readiness_registration():
    manager = ReadinessManager()
    entity_id = manager.register_readiness("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_readiness(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_readiness_integrity():
    manager = ReadinessManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
