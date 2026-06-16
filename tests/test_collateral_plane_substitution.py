import pytest
from app.collateral_plane.substitution import SubstitutionManager

def test_substitution_registration():
    manager = SubstitutionManager()
    entity_id = manager.register_substitution("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_substitution(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_substitution_integrity():
    manager = SubstitutionManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
