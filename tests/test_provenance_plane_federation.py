import pytest
from app.federation_plane.portability import check_portability_provenance

def test_portable_verdict_without_provenance_blocked():
    assert "BLOCKER/CAUTION" in check_portability_provenance("fed-1", False)
    assert "TRUSTED" in check_portability_provenance("fed-2", True)
