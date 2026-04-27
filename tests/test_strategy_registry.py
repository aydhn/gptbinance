import pytest
from app.strategies.registry import StrategyRegistry
from app.strategies.base import BaseStrategy
from app.strategies.models import (
    StrategySpec,
    StrategyContext,
    StrategyEvaluationResult,
)
from app.strategies.enums import StrategyType
from app.strategies.exceptions import InvalidStrategySpecError


class DummyStrategy(BaseStrategy):
    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        return StrategyEvaluationResult(
            strategy_name=self.name, symbol=context.symbol, timestamp=context.timestamp
        )


def test_registry_registration():
    StrategyRegistry.register("dummy", DummyStrategy)
    assert "dummy" in StrategyRegistry.list_registered_implementations()

    spec = StrategySpec(name="dummy", strategy_type=StrategyType.UNKNOWN)
    StrategyRegistry.register_spec(spec)

    assert spec in StrategyRegistry.list_active_specs()
    assert StrategyRegistry.get_spec("dummy") == spec


def test_invalid_spec():
    with pytest.raises(InvalidStrategySpecError):
        StrategyRegistry.register_spec(
            StrategySpec(name="non_existent", strategy_type=StrategyType.UNKNOWN)
        )


def test_create_instance():
    StrategyRegistry.register("dummy", DummyStrategy)
    spec = StrategySpec(name="dummy", strategy_type=StrategyType.UNKNOWN)
    StrategyRegistry.register_spec(spec)

    instance = StrategyRegistry.create_instance(spec)
    assert isinstance(instance, DummyStrategy)
    assert instance.name == "dummy"
