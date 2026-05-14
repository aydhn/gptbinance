import abc
from typing import Dict, Any

class ContinuityRegistryBase(abc.ABC):
    @abc.abstractmethod
    def register(self, obj: Any) -> None:
        pass

class RestoreEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, record: Any) -> Dict[str, Any]:
        pass

class FailoverEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, record: Any) -> Dict[str, Any]:
        pass

class TrustEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, record: Any) -> str:
        pass
