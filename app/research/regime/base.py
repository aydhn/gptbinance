from typing import List
from abc import ABC, abstractmethod

from app.research.regime.models import RegimeEvaluationResult, RegimeFeatureBundle
from app.research.regime.enums import RegimeFamily


class BaseRegimeEvaluator(ABC):
    """
    Base contract for all regime evaluators.
    An evaluator takes a bundle of features and returns a RegimeEvaluationResult.
    """

    @property
    @abstractmethod
    def family(self) -> RegimeFamily:
        """The regime family this evaluator belongs to."""
        pass

    @property
    @abstractmethod
    def required_features(self) -> List[str]:
        """List of feature names required to run this evaluator."""
        pass

    @property
    @abstractmethod
    def min_history_required(self) -> int:
        """Minimum number of historical bars required for stability."""
        pass

    @abstractmethod
    def evaluate(
        self, bundle: RegimeFeatureBundle, history: List[RegimeFeatureBundle] = None
    ) -> RegimeEvaluationResult:
        """
        Evaluate the current regime based on features.
        History is optional but can be used for things like recent stability.
        """
        pass
