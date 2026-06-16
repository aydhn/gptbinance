import pytest
from app.collateral_plane.trust import TrustManager

def test_trust_registration():
    manager = TrustManager()
    entity_id = manager.register_trust("TEST_001", {"data": "valid"})
    assert entity_id == "TEST_001"

    record = manager.get_trust(entity_id)
    assert record["data"] == "valid"
    assert "lineage_refs" in record
    assert any("registered" in ref for ref in record["lineage_refs"])

def test_trust_integrity():
    manager = TrustManager()
    # Missing entity
    cautions = manager.evaluate_integrity("MISSING_001")
    assert len(cautions) > 0
