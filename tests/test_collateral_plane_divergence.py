import pytest
from app.collateral_plane.divergence import DivergenceManager

def test_divergence_registration():
    manager = DivergenceManager()
    entity_id = manager.register_divergence("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_divergence(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_divergence_integrity():
    manager = DivergenceManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
