import pytest
from app.contract_plane.runtime_observations import check_contract_runtime_provenance

def test_verified_change_without_effect_caution():
    assert "CAUTION" in check_contract_runtime_provenance("obs-1", [])
    assert "TRUSTED" in check_contract_runtime_provenance("obs-2", ["ref1"])
