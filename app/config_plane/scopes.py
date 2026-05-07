from app.config_plane.models import ConfigScope
from app.config_plane.enums import ScopeClass
from app.config_plane.exceptions import ScopeMismatchError


class ScopeResolver:
    @staticmethod
    def is_compatible(
        target_scope: ConfigScope, layer_allowed_scopes: list[ScopeClass]
    ) -> bool:
        if target_scope.scope_class not in layer_allowed_scopes:
            raise ScopeMismatchError(
                f"Scope {target_scope.scope_class} not allowed for layer"
            )
        return True
