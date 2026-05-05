import pytest
from app.experiments.scopes import ScopeResolver
from app.experiments.models import ExperimentScope
from app.experiments.enums import ScopeType
from app.experiments.exceptions import ExperimentPolicyViolationError


def test_scope_resolver():
    resolver = ScopeResolver()

    valid_scope = ExperimentScope(
        scope_type=ScopeType.PROFILE,
        allowed_profiles=["paper"],
        allowed_symbols=["BTCUSDT"],
        time_windows=[],
    )
    assert resolver.validate_scope(valid_scope)

    invalid_scope = ExperimentScope(
        scope_type=ScopeType.PROFILE,
        allowed_profiles=["live"],
        allowed_symbols=["BTCUSDT"],
        time_windows=[],
    )
    with pytest.raises(ExperimentPolicyViolationError):
        resolver.validate_scope(invalid_scope)
