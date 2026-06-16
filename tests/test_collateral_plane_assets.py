import pytest
from app.collateral_plane.assets import AssetsManager

def test_assets_registration():
    manager = AssetsManager()
    entity_id = manager.register_assets("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_assets(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_assets_integrity():
    manager = AssetsManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
