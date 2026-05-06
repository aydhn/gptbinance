from uuid import uuid4
from app.identity.models import PrincipalRecord
from app.identity.enums import PrincipalType, PrincipalStatus
from app.identity.principals import principal_registry


def test_principal_registration():
    p = PrincipalRecord(name="Test User", principal_type=PrincipalType.HUMAN)
    principal_registry.register_principal(p)
    resolved = principal_registry.resolve_principal(p.id)
    assert resolved is not None
    assert resolved.name == "Test User"
    assert resolved.status == PrincipalStatus.ACTIVE
