from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.drift_plane.enums import (
    DriftClass, BaselineClass, SignalClass, BreachClass, GuardrailClass,
    RecurrenceClass, RestrictionClass, ScarClass, RenormalizationClass,
    EquivalenceVerdict, TrustVerdict
)

class DriftObjectRef(BaseModel):
    drift_id: str
    class_type: DriftClass

class BaselineScopeRecord(BaseModel):
    included_domains: List[str] = Field(default_factory=list)
    federated_scopes: List[str] = Field(default_factory=list)
    disputed_scopes: List[str] = Field(default_factory=list)
    cautions: List[str] = Field(default_factory=list)

class BaselineRecord(BaseModel):
    baseline_id: str
    class_type: BaselineClass
    scope: BaselineScopeRecord
    established_at: datetime
    owner: str
    lineage_refs: List[str] = Field(default_factory=list)

class DriftSignalRecord(BaseModel):
    signal_id: str
    class_type: SignalClass
    detected_at: datetime
    source: str
    lineage_refs: List[str] = Field(default_factory=list)

class MetricErosionRecord(BaseModel):
    erosion_id: str
    erosion_type: str  # progressive, stepwise, domain, buried
    metric_name: str
    lineage_refs: List[str] = Field(default_factory=list)

class ThresholdBreachRecord(BaseModel):
    breach_id: str
    class_type: BreachClass
    threshold_id: str
    breached_at: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class GuardrailDeviationRecord(BaseModel):
    deviation_id: str
    class_type: GuardrailClass
    guardrail_id: str
    deviated_at: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class ControlDriftRecord(BaseModel):
    drift_id: str
    drift_type: str  # board, veto, governance_creep, hidden
    lineage_refs: List[str] = Field(default_factory=list)

class AuthorityDriftRecord(BaseModel):
    drift_id: str
    drift_type: str  # expanded, decayed, conflicted, broken
    lineage_refs: List[str] = Field(default_factory=list)

class CapabilityRegressionRecord(BaseModel):
    regression_id: str
    regression_type: str  # degraded, intermittent, false_restored
    capability_id: str
    lineage_refs: List[str] = Field(default_factory=list)

class ReliabilityRegressionRecord(BaseModel):
    regression_id: str
    regression_type: str  # latent, recurring, rebound_failure
    lineage_refs: List[str] = Field(default_factory=list)

class ComplianceDriftRecord(BaseModel):
    drift_id: str
    drift_type: str  # procedural, authorization, reporting
    lineage_refs: List[str] = Field(default_factory=list)

class BeneficiaryImpactDriftRecord(BaseModel):
    drift_id: str
    drift_type: str  # re_emerging, access, fairness, hidden
    impacted_beneficiaries: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ScarReactivationRecord(BaseModel):
    scar_id: str
    class_type: ScarClass
    reactivated_at: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class RecurrenceTriggerRecord(BaseModel):
    trigger_id: str
    class_type: RecurrenceClass
    triggered_at: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class RestrictionReimpositionRecord(BaseModel):
    restriction_id: str
    class_type: RestrictionClass
    reimposed_at: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class RenormalizationPrerequisiteRecord(BaseModel):
    prereq_id: str
    class_type: RenormalizationClass
    satisfied: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class DriftComparisonRecord(BaseModel):
    comparison_id: str
    comparison_type: str  # baseline_vs_current, monitored_vs_controlled, local_vs_federated, stable_vs_recurrence_prone
    result_summary: str
    lineage_refs: List[str] = Field(default_factory=list)

class DriftObservationReport(BaseModel):
    drifts: List[Dict[str, Any]] = Field(default_factory=list)
    proof_notes: List[str] = Field(default_factory=list)

class DriftForecastReport(BaseModel):
    forecast_type: str  # recurrence_likelihood, erosion_acceleration, guardrail_retirement_risk, beneficiary_rebound, authority_creep
    uncertainty_class: str
    details: str

class DriftDebtRecord(BaseModel):
    debt_id: str
    debt_type: str  # hidden_drift, baseline_gaming, guardrail_retirement, recurrence_theater, scar_denial
    severity: str

class DriftEquivalenceReport(BaseModel):
    verdict: EquivalenceVerdict
    blockers: List[str] = Field(default_factory=list)
    divergence_sources: List[str] = Field(default_factory=list)

class DriftDivergenceReport(BaseModel):
    divergences: List[Dict[str, Any]] = Field(default_factory=list)
    blast_radius: str

class DriftTrustVerdict(BaseModel):
    verdict: TrustVerdict
    blockers: List[str] = Field(default_factory=list)
    caveats: List[str] = Field(default_factory=list)
    factors: Dict[str, str] = Field(default_factory=dict)

class DriftAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    timestamp: datetime
    details: str

class DriftArtifactManifest(BaseModel):
    manifest_id: str
    hashes: Dict[str, str] = Field(default_factory=dict)
    lineage_refs: List[str] = Field(default_factory=list)

class DriftObject(BaseModel):
    drift_id: str
    class_type: DriftClass
    owner: str
    scope: str
    baseline_posture: str
    recurrence_posture: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DriftRecord(BaseModel):
    drift_id: str
    lifecycle_state: str  # observed, active, restricted, resolved
    proof_notes: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)
