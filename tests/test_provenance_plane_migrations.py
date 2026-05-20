import pytest
from app.migration_plane.verification import check_migration_provenance

def test_contract_mismatch_explicit_caution():
    assert "TRUST_DEGRADED" in check_migration_provenance("mig-1", True)
    assert "TRUSTED" in check_migration_provenance("mig-2", False)
