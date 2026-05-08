from typing import Dict, List, Optional
from app.strategy_plane.models import StrategyDefinition, StrategyRef
from app.strategy_plane.exceptions import InvalidStrategyDefinition


class CanonicalStrategyRegistry:
    def __init__(self):
        self._strategies: Dict[str, StrategyDefinition] = {}

    def register(self, definition: StrategyDefinition) -> None:
        if definition.strategy_id in self._strategies:
            raise InvalidStrategyDefinition(
                f"Strategy {definition.strategy_id} already registered."
            )

        # enforce required fields
        if not definition.hypothesis_ref or not definition.thesis_ref:
            raise InvalidStrategyDefinition(
                "Strategy must have hypothesis and thesis references."
            )
        if not definition.signal_contracts:
            raise InvalidStrategyDefinition(
                "Strategy must define at least one signal contract."
            )

        self._strategies[definition.strategy_id] = definition

    def get(self, strategy_id: str) -> Optional[StrategyDefinition]:
        return self._strategies.get(strategy_id)

    def list_all(self) -> List[StrategyDefinition]:
        return list(self._strategies.values())

    def get_by_family(self, family) -> List[StrategyDefinition]:
        return [s for s in self._strategies.values() if s.family == family]
