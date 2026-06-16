import pytest
from app.collateral_plane.pledgors import PledgorsManager

def test_pledgors_registration():
    manager = PledgorsManager()
    entity_id = manager.register_pledgors("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_pledgors(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_pledgors_integrity():
    manager = PledgorsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
