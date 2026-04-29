from abc import ABC, abstractmethod
from typing import List, Optional
from app.risk.models import (
    RiskEvaluationRequest,
    PositionSizingResult,
    RiskRejectionReason,
    RiskContext,
)


class BaseRiskPolicy(ABC):
    @abstractmethod
    def evaluate(self, request: RiskEvaluationRequest) -> Optional[RiskRejectionReason]:
        """Return a rejection reason if the policy is violated, else None."""
        pass


class BaseRiskGuard(ABC):
    @abstractmethod
    def check(self, request: RiskEvaluationRequest) -> Optional[RiskRejectionReason]:
        """Return a rejection reason if the guard condition is met, else None."""
        pass


class BasePositionSizer(ABC):
    @abstractmethod
    def calculate_size(self, request: RiskEvaluationRequest) -> PositionSizingResult:
        """Calculate the appropriate position size."""
        pass


class BaseRiskEvaluator(ABC):
    @abstractmethod
    def evaluate_intent(self, request: RiskEvaluationRequest):
        """Evaluate an intent through the full risk pipeline."""
        pass
