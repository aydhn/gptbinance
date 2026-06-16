import pytest
from app.collateral_plane.forecasting import ForecastingManager

def test_forecasting_registration():
    manager = ForecastingManager()
    entity_id = manager.register_forecasting("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_forecasting(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_forecasting_integrity():
    manager = ForecastingManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
