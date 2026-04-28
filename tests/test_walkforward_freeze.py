import pytest
from app.backtest.walkforward.freeze import FreezeManager
from app.backtest.walkforward.models import FrozenStrategyBundle
from app.strategies.models import StrategySpec
from app.strategies.enums import StrategyType


def test_freeze_verify():
    spec = StrategySpec(
        name="strat1",
        strategy_type=StrategyType.TREND_FOLLOW,
        required_features=[],
        parameters={"a": 1},
    )
    bundle = FrozenStrategyBundle(spec=spec, frozen_at="now", metadata={})

    manager = FreezeManager()
    snapshot = manager.freeze(bundle)

    # Verification should pass
    assert manager.verify(bundle, snapshot) is True

    # Tamper with the spec
    bundle.spec.parameters["a"] = 2

    # Verification should fail
    assert manager.verify(bundle, snapshot) is False
