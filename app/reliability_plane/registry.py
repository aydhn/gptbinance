from datetime import datetime
from typing import Dict, List, Optional

from .base import ReliabilityRegistryBase
from .exceptions import InvalidReliabilityDefinition
from .models import (ReliabilityObjective, ReliabilityService, SliDefinition,
                     SloDefinition)


class CanonicalReliabilityRegistry(ReliabilityRegistryBase):
    def __init__(self):
        self._services: Dict[str, ReliabilityService] = {}
        self._objectives: Dict[str, ReliabilityObjective] = {}
        self._slis: Dict[str, SliDefinition] = {}
        self._slos: Dict[str, SloDefinition] = {}
        self._required_families = [
            "execution_reliability",
            "risk_refresh_reliability",
            "release_rollout_reliability",
            "workflow_completion_reliability",
            "market_data_freshness_reliability",
            "model_serving_reliability",
            "feature_freshness_reliability",
            "ledger_reconcile_reliability",
            "incident_recovery_reliability",
            "activation_progression_reliability",
            "observability_integrity_reliability",
            "control_action_reliability",
        ]

    def register_service(self, service: ReliabilityService) -> None:
        if not service.service_id:
            raise InvalidReliabilityDefinition("Service ID cannot be empty.")
        self._services[service.service_id] = service

    def get_service(self, service_id: str) -> Optional[ReliabilityService]:
        return self._services.get(service_id)

    def list_services(self) -> List[ReliabilityService]:
        return list(self._services.values())

    def register_objective(self, objective: ReliabilityObjective) -> None:
        if not objective.objective_id:
            raise InvalidReliabilityDefinition("Objective ID cannot be empty.")
        if objective.service_id not in self._services:
            raise InvalidReliabilityDefinition(
                f"Unknown service_id {objective.service_id}"
            )
        self._objectives[objective.objective_id] = objective

    def get_objective(self, objective_id: str) -> Optional[ReliabilityObjective]:
        return self._objectives.get(objective_id)

    def list_objectives(self) -> List[ReliabilityObjective]:
        return list(self._objectives.values())

    def register_sli(self, sli: SliDefinition) -> None:
        if not sli.sli_id:
            raise InvalidReliabilityDefinition("SLI ID cannot be empty.")
        if sli.service_id not in self._services:
            raise InvalidReliabilityDefinition(f"Unknown service_id {sli.service_id}")
        if not sli.telemetry_support_refs:
            raise InvalidReliabilityDefinition(
                "Telemetry support is required for SLI definition."
            )
        self._slis[sli.sli_id] = sli

    def get_sli(self, sli_id: str) -> Optional[SliDefinition]:
        return self._slis.get(sli_id)

    def list_slis(self) -> List[SliDefinition]:
        return list(self._slis.values())

    def register_slo(self, slo: SloDefinition) -> None:
        if not slo.slo_id:
            raise InvalidReliabilityDefinition("SLO ID cannot be empty.")
        if slo.sli_id not in self._slis:
            raise InvalidReliabilityDefinition(f"Unknown sli_id {slo.sli_id}")
        self._slos[slo.slo_id] = slo

    def get_slo(self, slo_id: str) -> Optional[SloDefinition]:
        return self._slos.get(slo_id)

    def list_slos(self) -> List[SloDefinition]:
        return list(self._slos.values())
