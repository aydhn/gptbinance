from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .models import (ErrorBudgetPolicy, ReliabilityObjective,
                     ReliabilityService, ReliabilityStateSnapshot,
                     ReliabilityTrustVerdictReport, SliDefinition,
                     SloDefinition)


class ReliabilityRegistryBase:
    def register_service(self, service: ReliabilityService) -> None:
        pass

    def get_service(self, service_id: str) -> Optional[ReliabilityService]:
        pass

    def register_objective(self, objective: ReliabilityObjective) -> None:
        pass

    def register_sli(self, sli: SliDefinition) -> None:
        pass

    def register_slo(self, slo: SloDefinition) -> None:
        pass


class BudgetEvaluatorBase:
    def evaluate_budget(self, policy_id: str) -> Any:
        pass


class DependencyEvaluatorBase:
    def evaluate_dependencies(self, service_id: str) -> Any:
        pass


class TrustEvaluatorBase:
    def evaluate_trust(self, service_id: str) -> ReliabilityTrustVerdictReport:
        pass
