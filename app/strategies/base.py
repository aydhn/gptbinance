from abc import ABC, abstractmethod
from typing import Dict, List, Any

from app.strategies.models import (
    StrategySpec,
    StrategyContext,
    StrategyEvaluationResult,
    StrategyStateSnapshot,
)


class BaseStrategy(ABC):
    """
    Base class for all strategy implementations.
    Defines the contract for strategy evaluation.
    """

    def __init__(self, spec: StrategySpec):
        self.spec = spec
        self.state: Dict[str, Any] = {}

    @property
    def name(self) -> str:
        return self.spec.name

    @property
    def required_features(self) -> List[str]:
        return self.spec.required_features

    def is_ready(self, context: StrategyContext) -> bool:
        """
        Check if the strategy has all required features and enough history to evaluate.
        """
        for feature in self.required_features:
            if feature not in context.features:
                return False
        # In a real implementation, we would check if we have min_history data points.
        # For now, we assume the provided features represent the current state correctly.
        return True

    @abstractmethod
    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        """
        Evaluate the strategy logic given the current context.
        Returns an evaluation result containing any signals or intents.
        """
        pass

    def get_state_snapshot(self) -> StrategyStateSnapshot:
        """
        Return a snapshot of the strategy's internal state.
        """
        return StrategyStateSnapshot(
            strategy_name=self.name,
            symbol="any",  # Placeholder, symbol is context specific
            internal_state=self.state,
        )

    def restore_state(self, snapshot: StrategyStateSnapshot):
        """
        Restore the strategy's internal state from a snapshot.
        """
        if snapshot.strategy_name == self.name:
            self.state = snapshot.internal_state.copy()
