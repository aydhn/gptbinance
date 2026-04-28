from typing import Dict, List
from app.research.regime.base import BaseRegimeEvaluator
from app.research.regime.enums import RegimeFamily
from app.research.regime.exceptions import InvalidRegimeSpecError


class RegimeRegistry:
    def __init__(self):
        self._evaluators: Dict[str, BaseRegimeEvaluator] = {}
        self._family_map: Dict[RegimeFamily, List[str]] = {
            family: [] for family in RegimeFamily
        }

    def register(self, name: str, evaluator: BaseRegimeEvaluator):
        if name in self._evaluators:
            raise InvalidRegimeSpecError(f"Evaluator '{name}' is already registered.")

        self._evaluators[name] = evaluator
        self._family_map[evaluator.family].append(name)

    def get_evaluator(self, name: str) -> BaseRegimeEvaluator:
        if name not in self._evaluators:
            raise InvalidRegimeSpecError(f"Evaluator '{name}' not found in registry.")
        return self._evaluators[name]

    def get_evaluators_by_family(
        self, family: RegimeFamily
    ) -> List[BaseRegimeEvaluator]:
        return [self._evaluators[name] for name in self._family_map[family]]

    def list_all_evaluators(self) -> List[str]:
        return list(self._evaluators.keys())


# Global registry instance
regime_registry = RegimeRegistry()
