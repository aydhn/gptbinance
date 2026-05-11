from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class PolicyRegistryBase(ABC):
    @abstractmethod
    def register(self, policy: Any):
        pass

    @abstractmethod
    def get(self, policy_id: str) -> Any:
        pass


class PolicyEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, subject: Any, action: Any, resource: Any, context: Any) -> Any:
        pass


class PrecedenceEvaluatorBase(ABC):
    @abstractmethod
    def resolve(self, rules: List[Any], context: Any) -> Any:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def assess_trust(self) -> Any:
        pass
