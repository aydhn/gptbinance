from app.identity_plane.models import *
from app.identity_plane.enums import *
from app.identity_plane.registry import CanonicalPrincipalRegistry
from app.identity_plane.authorization import AuthorizationEngine

def test_registry():

    reg = CanonicalPrincipalRegistry()
    reg.register_principal(PrincipalDefinition(principal_id="u1", principal_class=PrincipalClass.HUMAN_OPERATOR))
    assert "u1" in reg.principals
