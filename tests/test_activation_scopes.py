import pytest
from app.activation.scopes import ScopeEnforcer
from app.activation.models import ActivationScope
from app.activation.exceptions import ScopeViolationError


def test_scope_within_limits():
    allowed = ActivationScope(allowed_symbols=["BTCUSDT", "ETHUSDT"], ttl_seconds=3600)
    requested = ActivationScope(allowed_symbols=["BTCUSDT"], ttl_seconds=1800)
    assert ScopeEnforcer.is_within_scope(requested, allowed) is True


def test_scope_exceeds_limits():
    allowed = ActivationScope(allowed_symbols=["BTCUSDT"], ttl_seconds=3600)
    requested = ActivationScope(
        allowed_symbols=["BTCUSDT", "ETHUSDT"], ttl_seconds=1800
    )
    assert ScopeEnforcer.is_within_scope(requested, allowed) is False

    with pytest.raises(ScopeViolationError):
        ScopeEnforcer.validate_activation(requested, allowed)
