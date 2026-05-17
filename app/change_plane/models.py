from typing import List, Optional, Dict, Any
from datetime import datetime

from app.change_plane.enums import (
    ChangeClass, RequestClass, ApprovalClass, WindowClass,
    BlastRadiusClass, ExecutionClass, RollbackClass,
    VerificationClass, FreezeClass, ExceptionClass,
    EquivalenceVerdict, ChangeTrustVerdict
)

class BaseModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def dict(self):
        res = {}
        for k, v in self.__dict__.items():
            if hasattr(v, 'dict'):
                res[k] = v.dict()
            elif isinstance(v, list):
                res[k] = [i.dict() if hasattr(i, 'dict') else i for i in v]
            else:
                res[k] = v
        return res

class ChangeObjectRef(BaseModel):
    change_id: str
    name: str
    change_class: ChangeClass

class ChangeRequestRecord(BaseModel):
    request_id: str
    change_id: str
    request_class: RequestClass
    initiating_reason: str
    target_surfaces: List[str]
    expected_benefit: str
    expected_downside: str
    requester_metadata: Dict[str, Any]
    requested_at: datetime

class ChangeClassificationRecord(BaseModel):
    change_id: str
    change_class: ChangeClass
    caveats: List[str]
    reclassification_lineage_refs: List[str]

class ImpactAssessmentRecord(BaseModel):
    change_id: str
    system_impact: str
    customer_business_impact: str
    reliability_security_compliance_impact: str
    capacity_cost_impact: str
    residual_impact_notes: str

class BlastRadiusRecord(BaseModel):
    change_id: str
    radius_class: BlastRadiusClass
    operator_burden_impact: str
    unknown_radius_warnings: List[str]

class ApprovalChainRecord(BaseModel):
    change_id: str
    approval_class: ApprovalClass
    approvers: List[str]
    approved_at: Optional[datetime]
    conflict_notes: List[str]

class ChangeWindowRecord(BaseModel):
    window_id: str
    change_id: str
    window_class: WindowClass
    start_time: datetime
    end_time: datetime
    constraints: List[str]

class ChangeCalendarSnapshot(BaseModel):
    snapshot_id: str
    active_windows: List[str]
    blackout_periods: List[str]
    freeze_windows: List[str]
    snapshot_at: datetime

class ChangeDependencyRecord(BaseModel):
    change_id: str
    prerequisite_changes: List[str]
    verification_dependency: List[str]
    rollback_dependency: List[str]
    downstream_dependency: List[str]

class FreezeConstraintRecord(BaseModel):
    freeze_id: str
    freeze_class: FreezeClass
    active: bool
    bypass_evidence: Optional[str]

class RollbackPlanRecord(BaseModel):
    change_id: str
    rollback_class: RollbackClass
    feasibility: str
    prerequisites: List[str]
    tested_posture: str
    caveats: List[str]

class RollforwardPlanRecord(BaseModel):
    change_id: str
    strategy: str
    compensating_changes: List[str]
    risks: List[str]

class ChangeExecutionRecord(BaseModel):
    execution_id: str
    change_id: str
    execution_class: ExecutionClass
    receipt: Optional[str]
    executed_at: datetime

class ChangeVerificationRecord(BaseModel):
    verification_id: str
    change_id: str
    verification_class: VerificationClass
    sufficiency_notes: str
    verified_at: Optional[datetime]

class ChangeObservationRecord(BaseModel):
    observation_id: str
    change_id: str
    quiet_period_end: datetime
    latent_issues: List[str]

class ChangeExceptionRecord(BaseModel):
    exception_id: str
    change_id: str
    exception_class: ExceptionClass
    expiry: datetime
    residual_risk: str

class ChangeCollisionRecord(BaseModel):
    collision_id: str
    change_id: str
    colliding_change_ids: List[str]
    contention_type: str
    resolution_notes: str

class ChangeRiskRecord(BaseModel):
    change_id: str
    implementation_risk: str
    rollback_risk: str
    verification_risk: str
    operator_error_risk: str
    coupled_change_risk: str

class ChangeForecastReport(BaseModel):
    forecast_id: str
    collision_likelihood: str
    verification_lag: str
    rollback_likelihood: str
    emergency_normalization: str

class ChangeDebtRecord(BaseModel):
    change_id: str
    debt_type: str
    severity: str

class ChangeEquivalenceReport(BaseModel):
    change_id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str]

class ChangeDivergenceReport(BaseModel):
    change_id: str
    divergence_type: str
    severity: str

class ChangeTrustVerdictModel(BaseModel):
    change_id: str
    verdict: ChangeTrustVerdict
    factors: Dict[str, str]
    breakdown_mandatory: bool
    generated_at: datetime

class ChangeAuditRecord(BaseModel):
    change_id: str
    audit_trail: List[str]

class ChangeArtifactManifest(BaseModel):
    change_id: str
    manifest_hash: str
    lineage_refs: List[str]

class ChangeObject(BaseModel):
    change_id: str
    name: str
    owner: str
    change_class: ChangeClass
    target_surface: str
    request: Optional[ChangeRequestRecord]
    impact: Optional[ImpactAssessmentRecord]
    blast_radius: Optional[BlastRadiusRecord]
    approval: Optional[ApprovalChainRecord]
    window: Optional[ChangeWindowRecord]
    rollback: Optional[RollbackPlanRecord]
    execution: Optional[ChangeExecutionRecord]
    verification: Optional[ChangeVerificationRecord]
    trust_verdict: Optional[ChangeTrustVerdictModel]

class ChangeRegistryModel(BaseModel):
    changes: List[ChangeObject]
