from abc import ABC, abstractmethod
from typing import List, Optional


class MetricCollectorBase(ABC):
    @abstractmethod
    def record(self, sample) -> None:
        pass


class HealthAggregatorBase(ABC):
    @abstractmethod
    def evaluate(self) -> None:
        pass


class AlertEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self) -> None:
        pass


class CorrelatorBase(ABC):
    @abstractmethod
    def correlate(self) -> None:
        pass


class DigestBuilderBase(ABC):
    @abstractmethod
    def build(self) -> None:
        pass
