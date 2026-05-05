from app.remediation.models import RemediationScope


class ScopeResolver:
    def resolve_inheritance(self, scope: RemediationScope) -> RemediationScope:
        # Resolve inherited scopes.
        # For instance, if symbol is specified, profile should usually be present too if applicable.
        # This is a simplified mock.
        resolved = RemediationScope(
            workspace=scope.workspace,
            profile=scope.profile,
            symbol=scope.symbol,
            run_id=scope.run_id,
        )
        return resolved

    def check_boundary_violation(
        self, scope1: RemediationScope, scope2: RemediationScope
    ) -> bool:
        # Cross-profile contamination guard.
        if scope1.workspace != scope2.workspace:
            return True
        if scope1.profile and scope2.profile and scope1.profile != scope2.profile:
            return True
        return False
