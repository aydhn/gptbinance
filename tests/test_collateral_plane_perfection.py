import pytest
from app.collateral_plane.perfection import PerfectionManager

def test_perfection_registration():
    manager = PerfectionManager()
    entity_id = manager.register_perfection("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_perfection(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_perfection_integrity():
    manager = PerfectionManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
