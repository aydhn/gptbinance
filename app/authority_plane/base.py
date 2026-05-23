from abc import ABC, abstractmethod
from typing import Dict, Any

class AuthorityRegistryBase(ABC):
    @abstractmethod
    def register(self, authority: Any) -> str:
        pass

    @abstractmethod
    def get(self, authority_id: str) -> Any:
        pass

class LegitimacyEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, authority_id: str) -> Any:
        pass

class DelegationEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, delegation_id: str) -> Any:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, entity_id: str) -> Any:
        pass
