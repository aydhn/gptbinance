import pytest
from app.collateral_plane.eligibility import EligibilityManager

def test_eligibility_registration():
    manager = EligibilityManager()
    entity_id = manager.register_eligibility("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_eligibility(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_eligibility_integrity():
    manager = EligibilityManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
