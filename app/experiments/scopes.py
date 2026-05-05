from app.experiments.models import ExperimentScope
from app.experiments.exceptions import ExperimentPolicyViolationError
from app.experiments.enums import ScopeType


class ScopeResolver:
    def validate_scope(self, scope: ExperimentScope) -> bool:
        if "live" in scope.allowed_profiles:
            raise ExperimentPolicyViolationError(
                "Live profile is strictly forbidden in experiments."
            )

        if scope.scope_type == ScopeType.WORKSPACE and not scope.allowed_profiles:
            raise ExperimentPolicyViolationError(
                "Workspace scope requires explicit profiles."
            )

        return True

    def check_surface_allowed(self, scope: ExperimentScope, surface: str) -> bool:
        return surface not in scope.forbidden_surfaces
