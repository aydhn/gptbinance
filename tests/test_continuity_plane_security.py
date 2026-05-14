import pytest
from app.continuity_plane.security import ContinuitySecurityLinkage

def test_security_linkage():
    linkage = ContinuitySecurityLinkage()
    assert linkage is not None
