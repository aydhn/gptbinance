import pytest
from app.collateral_plane.comparisons import ComparisonsManager

def test_comparisons_registration():
    manager = ComparisonsManager()
    entity_id = manager.register_comparisons("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_comparisons(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_comparisons_integrity():
    manager = ComparisonsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
