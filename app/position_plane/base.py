from abc import ABC, abstractmethod
from typing import Dict, Any


class LotBuilderBase(ABC):
    @abstractmethod
    def build(self, fill_data: Dict[str, Any]) -> Any:
        pass


class PositionReducerBase(ABC):
    @abstractmethod
    def reduce(self, state: Any, lots: list) -> Any:
        pass


class PnlAttributionBase(ABC):
    @abstractmethod
    def attribute(self, state: Any, market_data: Any) -> Any:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, state: Any, reconciliation_data: Any) -> Any:
        pass
