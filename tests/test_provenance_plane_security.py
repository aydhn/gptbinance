import pytest
from app.security_plane.readiness import check_security_provenance

def test_secret_use_without_chain_blocked():
    assert "CAUTION" in check_security_provenance("sec-1", True, False)
    assert "CAUTION" in check_security_provenance("sec-2", False, True)
    assert "TRUSTED" in check_security_provenance("sec-3", False, False)
