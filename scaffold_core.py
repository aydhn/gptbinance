import os

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def write_file(p, c):
    ensure_dir(os.path.dirname(p))
    with open(p, "w") as f:
        f.write(c)

write_file("app/suspension_plane/models.py", '''from pydantic import BaseModel, Field
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
''')

write_file("app/suspension_plane/enums.py", '''from enum import Enum

class SuspensionClass(str, Enum):
    INCIDENT_SUSPENSION = "incident_suspension"
    DRIFT_CONTROL_SUSPENSION = "drift_control_suspension"
    AUTONOMY_QUARANTINE = "autonomy_quarantine_suspension"
    ORCHESTRATION_HOLD = "orchestration_hold_suspension"
    BENEFICIARY_PROTECTION = "beneficiary_protection_suspension"
    RELEASE_FREEZE = "release_freeze_suspension"
    MIGRATION_HOLD = "migration_hold_suspension"
    POLICY_PAUSE = "policy_pause_suspension"
    EVIDENCE_GAP = "evidence_gap_suspension"
    FEDERATED_DISCONNECT = "federated_disconnect_suspension"
    CROSS_PLANE_PROTECTIVE = "cross_plane_protective_suspension"


class TriggerClass(str, Enum):
    INCIDENT_TRIGGER = "incident_trigger"
    EVIDENCE_GAP = "evidence_gap_trigger"
    AUTHORITY_TRIGGER = "authority_trigger"
    BENEFICIARY_PROTECTION = "beneficiary_protection_trigger"

class ScopeClass(str, Enum):
    NARROW = "narrow_scope"
    BROAD = "broad_scope"
    DISPUTED = "disputed_scope"
    LEAKING = "leaking_scope"

class FreezeClass(str, Enum):
    EXECUTION = "execution_freeze"
    CHANGE = "change_freeze"
    DECISION = "decision_freeze"
    DATA = "data_freeze"

class QuarantineClass(str, Enum):
    BOUNDED = "bounded_quarantine"
    POROUS = "porous_quarantine"
    BENEFICIARY_AWARE = "beneficiary_aware_quarantine"

class ResidualClass(str, Enum):
    APPROVED = "approved_residual"
    EMERGENCY = "emergency_residual"
    HIDDEN = "hidden_residual"
    EXCESSIVE = "excessive_residual"

class ResumptionClass(str, Enum):
    COMPLETE = "complete_resumption"
    PARTIAL = "partial_resumption"
    STALE = "stale_resumption"
    UNSAFE = "unsafe_resumption"

class TimeboxClass(str, Enum):
    BOUNDED = "bounded_timebox"
    RENEWABLE = "renewable_timebox"
    STALE = "stale_timebox"
    MISSING = "missing_timebox"

class DebtClass(str, Enum):
    STALE_HOLD = "stale_hold_debt"
    BYPASS = "bypass_debt"
    INDEFINITE = "indefinite_suspension_debt"
    LEAKAGE = "leakage_debt"
    SHADOW = "shadow_execution_debt"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
''')

write_file("app/suspension_plane/exceptions.py", '''class SuspensionPlaneError(Exception): pass
class InvalidSuspensionObjectError(SuspensionPlaneError): pass
class InvalidSuspensionTriggerError(SuspensionPlaneError): pass
class InvalidSuspensionScopeError(SuspensionPlaneError): pass
class InvalidFreezeBoundaryError(SuspensionPlaneError): pass
class InvalidQuarantineError(SuspensionPlaneError): pass
class InvalidResumptionCriteriaError(SuspensionPlaneError): pass
class SuspensionTheaterViolation(SuspensionPlaneError): pass
class SuspensionStorageError(SuspensionPlaneError): pass
''')

print("Core files generated.")
