import pytest
from app.collateral_plane.equivalence import EquivalenceManager

def test_equivalence_registration():
    manager = EquivalenceManager()
    entity_id = manager.register_equivalence("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_equivalence(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_equivalence_integrity():
    manager = EquivalenceManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
