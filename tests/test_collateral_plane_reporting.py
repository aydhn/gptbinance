import pytest
from app.collateral_plane.reporting import ReportingManager

def test_reporting_registration():
    manager = ReportingManager()
    entity_id = manager.register_reporting("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_reporting(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_reporting_integrity():
    manager = ReportingManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
