from abc import ABC, abstractmethod

class RightsRegistryBase(ABC):
    @abstractmethod
    def register_right(self, right_id: str, data: dict): pass

class StandingEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_standing(self, claim_id: str) -> bool: pass

class ConsentEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_consent(self, consent_id: str) -> bool: pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self) -> dict: pass
