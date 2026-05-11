from app.identity_plane.models import *
from app.identity_plane.enums import *
from app.identity_plane.registry import CanonicalPrincipalRegistry
from app.identity_plane.authorization import AuthorizationEngine

def test_authorization():

    reg = CanonicalPrincipalRegistry()
    authz = AuthorizationEngine(reg)
    res = authz.evaluate("unknown", "cap1", "live")
    assert not res.is_allowed
