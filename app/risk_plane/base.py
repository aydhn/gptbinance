from abc import ABC, abstractmethod
from typing import List, Optional
from .models import RiskState, RiskLimitDefinition, RiskBreachRecord, RiskTrustVerdict


class RiskStateBuilderBase(ABC):
    @abstractmethod
    def build_state(self, domain: str, target_id: str, **kwargs) -> RiskState:
        pass


class LimitEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, state: RiskState, limit: RiskLimitDefinition
    ) -> Optional[RiskBreachRecord]:
        pass


class BreachClassifierBase(ABC):
    @abstractmethod
    def classify(
        self, state: RiskState, limit: RiskLimitDefinition
    ) -> RiskBreachRecord:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(
        self, states: List[RiskState], breaches: List[RiskBreachRecord]
    ) -> RiskTrustVerdict:
        pass
