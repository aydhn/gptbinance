from abc import ABC, abstractmethod
from typing import Dict, Any, List

class SecurityRegistryBase(ABC):
    @abstractmethod
    def register_security(self, security_object: Any) -> str:
        pass

    @abstractmethod
    def get_security(self, security_id: str) -> Any:
        pass

class CoverageEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_coverage(self, obligation_id: str) -> Dict[str, Any]:
        pass

class DrawEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_draw_conditions(self, security_id: str, amount: float) -> bool:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self, security_id: str) -> Any:
        pass
