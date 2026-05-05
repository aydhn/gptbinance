from app.remediation.scopes import ScopeResolver
from app.remediation.models import RemediationScope


def test_scope_boundary_violation():
    resolver = ScopeResolver()
    scope1 = RemediationScope(workspace="ws1", profile="p1")
    scope2 = RemediationScope(workspace="ws2", profile="p1")

    assert resolver.check_boundary_violation(scope1, scope2)

    scope3 = RemediationScope(workspace="ws1", profile="p1")
    scope4 = RemediationScope(workspace="ws1", profile="p2")

    assert resolver.check_boundary_violation(scope3, scope4)

    scope5 = RemediationScope(workspace="ws1", profile="p1")
    scope6 = RemediationScope(workspace="ws1", profile="p1")

    assert not resolver.check_boundary_violation(scope5, scope6)
