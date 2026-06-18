from abc import ABC, abstractmethod
from typing import Dict, Any, List

class NettingRegistryBase(ABC):
    @abstractmethod
    def register(self, netting_id: str, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get(self, netting_id: str) -> Dict[str, Any]:
        pass

class MutualityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, mutuality_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        pass

class CloseoutEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, closeout_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, netting_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        pass
