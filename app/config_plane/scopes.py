from app.config_plane.models import ConfigScope
from app.config_plane.enums import ScopeClass
from app.config_plane.exceptions import ScopeMismatchError


def is_scope_applicable(source_scope: ConfigScope, target_scope: ConfigScope) -> bool:
    """
    Checks if a source scope applies to a target scope.
    """
    if source_scope.scope_class == ScopeClass.GLOBAL:
        return True

    if source_scope.scope_class == target_scope.scope_class:
        if source_scope.target_id is None:  # Applies to all within this class
            return True
        return source_scope.target_id == target_scope.target_id

    # Hierarchical checks could go here (e.g. Workspace -> Profile -> Symbol)
    # For now, strict matching
    return False


def check_scope_allowed(
    layer_class_allowed_scopes: list[ScopeClass], requested_scope: ConfigScope
):
    if requested_scope.scope_class not in layer_class_allowed_scopes:
        raise ScopeMismatchError(
            f"Scope {requested_scope.scope_class} not allowed for layer."
        )
