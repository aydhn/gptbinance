from app.evidence_graph.models import ArtefactScope
from app.evidence_graph.exceptions import ScopeViolationError


class ScopeEnforcer:
    @staticmethod
    def validate_query_scope(user_scope: ArtefactScope, target_scope: ArtefactScope):
        if (
            user_scope.workspace
            and target_scope.workspace
            and user_scope.workspace != target_scope.workspace
        ):
            raise ScopeViolationError("Workspace mismatch")
        if (
            user_scope.profile
            and target_scope.profile
            and user_scope.profile != target_scope.profile
        ):
            raise ScopeViolationError("Profile mismatch")
        # Global can see all, but restricted cannot see global unless allowed
