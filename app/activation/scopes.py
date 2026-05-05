from app.activation.models import ActivationScope
from app.activation.exceptions import ScopeViolationError


class ScopeEnforcer:
    @staticmethod
    def is_within_scope(requested: ActivationScope, allowed: ActivationScope) -> bool:
        if allowed.allowed_symbols and not set(requested.allowed_symbols).issubset(
            set(allowed.allowed_symbols)
        ):
            return False
        if allowed.allowed_profiles and not set(requested.allowed_profiles).issubset(
            set(allowed.allowed_profiles)
        ):
            return False
        if allowed.allowed_sessions and not set(requested.allowed_sessions).issubset(
            set(allowed.allowed_sessions)
        ):
            return False
        if allowed.allowed_capital_tiers and not set(
            requested.allowed_capital_tiers
        ).issubset(set(allowed.allowed_capital_tiers)):
            return False
        if allowed.is_no_new_exposure and not requested.is_no_new_exposure:
            return False
        # TTL check - requested TTL should not exceed allowed TTL if allowed TTL is set
        if allowed.ttl_seconds is not None:
            if (
                requested.ttl_seconds is None
                or requested.ttl_seconds > allowed.ttl_seconds
            ):
                return False
        return True

    @staticmethod
    def validate_activation(requested: ActivationScope, allowed: ActivationScope):
        if not ScopeEnforcer.is_within_scope(requested, allowed):
            raise ScopeViolationError(
                "Requested activation scope exceeds the limits of the allowed board decision scope."
            )
