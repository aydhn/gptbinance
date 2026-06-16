import pytest
from app.collateral_plane.quality import QualityManager

def test_quality_registration():
    manager = QualityManager()
    entity_id = manager.register_quality("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_quality(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_quality_integrity():
    manager = QualityManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
