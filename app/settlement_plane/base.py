from abc import ABC, abstractmethod
from typing import Dict, Any
from app.settlement_plane.models import SettlementObject, SettlementTrustVerdict

class BaseSettlementRegistry(ABC):
    @abstractmethod
    def register_settlement(self, obj: SettlementObject) -> str:
        pass

    @abstractmethod
    def get_settlement(self, obj_id: str) -> SettlementObject:
        pass

class BaseInstructionEvaluator(ABC):
    @abstractmethod
    def evaluate(self, context: Dict[str, Any]) -> str:
        pass

class BaseFinalityEvaluator(ABC):
    @abstractmethod
    def evaluate(self, context: Dict[str, Any]) -> str:
        pass

class BaseTrustEvaluator(ABC):
    @abstractmethod
    def evaluate(self, obj_id: str, factors: Dict[str, Any]) -> SettlementTrustVerdict:
        pass
