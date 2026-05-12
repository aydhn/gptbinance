from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .enums import (BudgetClass, BurnRateClass, DegradedModeClass,
                    MaintenanceClass, ReliabilityEquivalenceVerdict,
                    ReliabilityObjectiveClass, ReliabilityServiceClass,
                    ReliabilityStateClass, ReliabilityTrustVerdict, SLIClass,
                    SLOClass)


class ReliabilityPlaneConfig(BaseModel):
    enabled: bool = True
    default_budget_class: BudgetClass = BudgetClass.STRICT
    storage_path: Optional[str] = None


class ReliabilityServiceRef(BaseModel):
    service_id: str


class ReliabilityObjectiveRef(BaseModel):
    objective_id: str


class DependencyGraphNode(BaseModel):
    service_id: str
    is_critical: bool
    weight: float = 1.0
    impact_notes: Optional[str] = None


class ReliabilityService(BaseModel):
    service_id: str
    service_class: ReliabilityServiceClass
    criticality_tier: int = 1
    owners: List[str] = Field(default_factory=list)
    lineage_refs: Dict[str, str] = Field(default_factory=dict)
    dependencies: List[DependencyGraphNode] = Field(default_factory=list)


class SliDefinition(BaseModel):
    sli_id: str
    sli_class: SLIClass
    service_id: str
    description: str
    telemetry_support_refs: List[str] = Field(default_factory=list)
    sufficiency_notes: Optional[str] = None


class SloDefinition(BaseModel):
    slo_id: str
    slo_class: SLOClass
    sli_id: str
    target_value: float
    window_seconds: int
    missing_slo_blocker: bool = False
    slo_proof_notes: Optional[str] = None


class ErrorBudgetPolicy(BaseModel):
    policy_id: str
    slo_id: str
    budget_class: BudgetClass
    depletion_threshold_alert: float = 0.8
    freeze_threshold: float = 1.0
    reset_policy_notes: str
    lineage_refs: Dict[str, str] = Field(default_factory=dict)


class ReliabilityObjective(BaseModel):
    objective_id: str
    service_id: str
    objective_class: ReliabilityObjectiveClass
    description: str
    slos: List[str] = Field(default_factory=list)
    non_goals: List[str] = Field(default_factory=list)
    proof_notes: Optional[str] = None


class ErrorBudgetSnapshot(BaseModel):
    snapshot_id: str
    policy_id: str
    timestamp: datetime
    total_budget: float
    consumed_budget: float
    remaining_budget: float
    is_exhausted: bool


class BurnRateReport(BaseModel):
    report_id: str
    policy_id: str
    timestamp: datetime
    burn_rate_class: BurnRateClass
    current_burn_rate: float
    short_window_burn: float
    long_window_burn: float
    forecast_exhaustion_time: Optional[datetime] = None
    proof_notes: Optional[str] = None


class ReliabilityWindow(BaseModel):
    window_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    window_type: str  # rolling, calendar, quiet, maintenance, canary
    caveats: Optional[str] = None


class DependencyImpactReport(BaseModel):
    report_id: str
    service_id: str
    upstream_failures: List[str] = Field(default_factory=list)
    downstream_impact_score: float
    proof_notes: Optional[str] = None


class MaintenanceWindowRecord(BaseModel):
    record_id: str
    service_id: str
    maintenance_class: MaintenanceClass
    start_time: datetime
    end_time: Optional[datetime] = None
    scope: str
    approvals: List[str] = Field(default_factory=list)
    masking_warnings: List[str] = Field(default_factory=list)


class DegradedModeRecord(BaseModel):
    record_id: str
    service_id: str
    mode_class: DegradedModeClass
    start_time: datetime
    exit_criteria: str
    is_overdue: bool = False
    lineage_refs: Dict[str, str] = Field(default_factory=dict)


class ReliabilityStateSnapshot(BaseModel):
    snapshot_id: str
    service_id: str
    timestamp: datetime
    state: ReliabilityStateClass
    reason: Optional[str] = None


class ReliabilityForecastReport(BaseModel):
    forecast_id: str
    service_id: str
    timestamp: datetime
    budget_exhaustion_risk: str
    recurrence_burden: float
    uncertainty_class: str


class ReliabilityIncidentLink(BaseModel):
    link_id: str
    service_id: str
    incident_id: str
    link_type: str


class ReliabilityRollup(BaseModel):
    rollup_id: str
    scope_type: str  # service, domain, environment
    scope_id: str
    timestamp: datetime
    overall_health_score: float
    exhausted_budgets: List[str] = Field(default_factory=list)
    active_degraded_modes: List[str] = Field(default_factory=list)


class ReliabilityEquivalenceReport(BaseModel):
    report_id: str
    service_id: str
    environments_compared: List[str]
    verdict: ReliabilityEquivalenceVerdict
    divergence_reasons: List[str] = Field(default_factory=list)
    proof_notes: Optional[str] = None


class ReliabilityDivergenceReport(BaseModel):
    report_id: str
    service_id: str
    divergence_source: str
    severity: str
    blast_radius: str


class ReliabilityTrustVerdictReport(BaseModel):
    verdict_id: str
    service_id: str
    timestamp: datetime
    verdict: ReliabilityTrustVerdict
    factors: Dict[str, Any] = Field(default_factory=dict)


class ReliabilityAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    action: str
    actor: str
    target_id: str
    details: Dict[str, Any] = Field(default_factory=dict)


class ReliabilityArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    service_refs: List[str] = Field(default_factory=list)
    objective_refs: List[str] = Field(default_factory=list)
    hash_value: str
