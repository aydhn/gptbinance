from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class SuspensionPlaneConfig(BaseModel):
    enabled: bool = True

class SuspensionObjectRef(BaseModel):
    suspension_id: str

class SuspensionObject(BaseModel):
    suspension_id: str
    suspension_class: str
    owner: str
    scope: str
    hold_posture: str
    resumption_posture: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SuspensionRecord(BaseModel):
    suspension_id: str
    state: str
    evidence_refs: List[str] = []

class SuspensionTriggerRecord(BaseModel):
    trigger_id: str
    suspension_id: str
    trigger_basis: str

class SuspensionScopeRecord(BaseModel):
    scope_id: str
    suspension_id: str
    boundaries: List[str]

class HoldConditionRecord(BaseModel):
    condition_id: str
    suspension_id: str
    basis: str

class FreezeBoundaryRecord(BaseModel):
    boundary_id: str
    suspension_id: str
    freeze_type: str

class QuarantineRecord(BaseModel):
    quarantine_id: str
    suspension_id: str
    strictness: str

class PartialSuspensionRecord(BaseModel):
    partial_id: str
    suspension_id: str
    allowed_zones: List[str]

class ResidualOperationRecord(BaseModel):
    operation_id: str
    suspension_id: str
    justification: str

class ResidualDutyRecord(BaseModel):
    duty_id: str
    suspension_id: str
    coverage: str

class BeneficiarySafeguardRecord(BaseModel):
    safeguard_id: str
    suspension_id: str
    impact_level: str

class AccessRestrictionRecord(BaseModel):
    restriction_id: str
    suspension_id: str

class ExecutionHoldRecord(BaseModel):
    hold_id: str
    suspension_id: str
    status: str

class DecisionFreezeRecord(BaseModel):
    freeze_id: str
    suspension_id: str

class DataFreezeRecord(BaseModel):
    freeze_id: str
    suspension_id: str

class ChangeFreezeRecord(BaseModel):
    freeze_id: str
    suspension_id: str

class ResumptionCriteriaRecord(BaseModel):
    criteria_id: str
    suspension_id: str
    required_evidence: List[str]

class UnsuspensionRecord(BaseModel):
    unsuspend_id: str
    suspension_id: str
    authorized_by: str

class TimeboxRecord(BaseModel):
    timebox_id: str
    suspension_id: str
    expires_at: datetime

class IndefiniteSuspensionRecord(BaseModel):
    indefinite_id: str
    suspension_id: str
    justification: str

class ShadowExecutionRecord(BaseModel):
    shadow_id: str
    suspension_id: str
    detected_paths: List[str]

class BypassAttemptRecord(BaseModel):
    bypass_id: str
    suspension_id: str

class ScopeLeakageRecord(BaseModel):
    leakage_id: str
    suspension_id: str

class SuspensionComparisonRecord(BaseModel):
    comparison_id: str
    suspension_id: str
    result: str

class SuspensionObservationReport(BaseModel):
    report_id: str
    suspension_id: str

class SuspensionForecastReport(BaseModel):
    forecast_id: str
    suspension_id: str

class SuspensionDebtRecord(BaseModel):
    debt_id: str
    suspension_id: str
    amount: float

class SuspensionEquivalenceReport(BaseModel):
    report_id: str
    suspension_id: str
    equivalence_verdict: str

class SuspensionDivergenceReport(BaseModel):
    report_id: str
    suspension_id: str
    divergence_score: float

class SuspensionTrustVerdict(BaseModel):
    verdict_id: str
    suspension_id: str
    verdict: str
    factors: Dict[str, Any]

class SuspensionAuditRecord(BaseModel):
    audit_id: str
    suspension_id: str
    action: str

class SuspensionArtifactManifest(BaseModel):
    manifest_id: str
    suspension_id: str
    hashes: Dict[str, str]
