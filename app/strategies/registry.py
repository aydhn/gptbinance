from typing import Dict, Type, List
from app.strategies.base import BaseStrategy
from app.strategies.models import StrategySpec
from app.strategies.exceptions import InvalidStrategySpecError


class StrategyRegistry:
    """
    Registry for strategy implementations.
    """

    _strategies: Dict[str, Type[BaseStrategy]] = {}
    _active_specs: Dict[str, StrategySpec] = {}

    @classmethod
    def register(cls, name: str, strategy_class: Type[BaseStrategy]):
        cls._strategies[name] = strategy_class

    @classmethod
    def get_class(cls, name: str) -> Type[BaseStrategy]:
        if name not in cls._strategies:
            raise InvalidStrategySpecError(
                f"Strategy implementation '{name}' not found in registry."
            )
        return cls._strategies[name]

    @classmethod
    def register_spec(cls, spec: StrategySpec):
        if spec.name not in cls._strategies:
            raise InvalidStrategySpecError(
                f"Cannot register spec for '{spec.name}': Implementation not found."
            )
        cls._active_specs[spec.name] = spec

    @classmethod
    def get_spec(cls, name: str) -> StrategySpec:
        if name not in cls._active_specs:
            raise InvalidStrategySpecError(f"Strategy spec '{name}' not found.")
        return cls._active_specs[name]

    @classmethod
    def create_instance(cls, spec: StrategySpec) -> BaseStrategy:
        strategy_class = cls.get_class(spec.name)
        return strategy_class(spec)

    @classmethod
    def list_registered_implementations(cls) -> List[str]:
        return list(cls._strategies.keys())

    @classmethod
    def list_active_specs(cls) -> List[StrategySpec]:
        return list(cls._active_specs.values())
