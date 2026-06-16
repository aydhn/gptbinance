import pytest
from app.collateral_plane.debt import DebtManager

def test_debt_registration():
    manager = DebtManager()
    entity_id = manager.register_debt("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_debt(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_debt_integrity():
    manager = DebtManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
