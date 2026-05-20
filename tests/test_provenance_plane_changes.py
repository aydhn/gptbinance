import pytest
from app.change_plane.verification import verify_change_provenance

def test_migration_accepted_with_gap_lowers_trust():
    assert "CAUTION" in verify_change_provenance("change-1", [])
    assert "TRUSTED" in verify_change_provenance("change-2", ["ref1"])
