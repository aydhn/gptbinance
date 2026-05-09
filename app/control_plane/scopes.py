from app.control_plane.enums import ScopeClass
from app.control_plane.exceptions import ScopeViolationError


class ScopeManager:
    def validate_scope(self, required: ScopeClass, provided: ScopeClass):
        if required != provided:
            raise ScopeViolationError(
                f"Required scope {required}, but provided {provided}"
            )

    def narrow_scope(self, scope: ScopeClass, scope_ref: str) -> str:
        return f"{scope.value}::{scope_ref}"
