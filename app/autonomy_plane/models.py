from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from app.autonomy_plane.enums import *

class AutonomyPlaneConfig(BaseModel):
    enabled: bool = True
    require_mandates: bool = True
    enforce_revocation: bool = True

class AutonomyObjectRef(BaseModel):
    id: str
    class_name: AutonomyClass

class AutonomyObject(BaseModel):
    id: str
    owner: str
    ref: AutonomyObjectRef
    scope: ScopeClass
    delegation_posture: str
    review_posture: ReviewClass

class AutonomyRecord(BaseModel):
    id: str
    object_id: str
    status: str
    proof_notes: List[str] = Field(default_factory=list)

class MandateRecord(BaseModel):
    id: str
    autonomy_id: str
    mandate_class: MandateClass
    lineage_refs: List[str] = Field(default_factory=list)

class DelegationGrantRecord(BaseModel):
    id: str
    autonomy_id: str
    grant_class: GrantClass
    lineage_refs: List[str] = Field(default_factory=list)

class ScopeRecord(BaseModel):
    id: str
    autonomy_id: str
    scope_class: ScopeClass
    lineage_refs: List[str] = Field(default_factory=list)

class ForbiddenSurfaceRecord(BaseModel):
    id: str
    autonomy_id: str
    surface_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ToolUseConstraintRecord(BaseModel):
    id: str
    autonomy_id: str
    constraint_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ConfidenceThresholdRecord(BaseModel):
    id: str
    autonomy_id: str
    confidence_class: ConfidenceClass
    lineage_refs: List[str] = Field(default_factory=list)

class HumanReviewGateRecord(BaseModel):
    id: str
    autonomy_id: str
    review_class: ReviewClass
    lineage_refs: List[str] = Field(default_factory=list)

class HumanOverrideRecord(BaseModel):
    id: str
    autonomy_id: str
    override_class: OverrideClass
    lineage_refs: List[str] = Field(default_factory=list)

class AutonomousActionRecord(BaseModel):
    id: str
    autonomy_id: str
    action_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class SelfHealingActionRecord(BaseModel):
    id: str
    autonomy_id: str
    heal_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class EscalationDutyRecord(BaseModel):
    id: str
    autonomy_id: str
    duty_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class EscalationRecord(BaseModel):
    id: str
    autonomy_id: str
    escalation_class: EscalationClass
    lineage_refs: List[str] = Field(default_factory=list)

class RevocationRecord(BaseModel):
    id: str
    autonomy_id: str
    revocation_class: RevocationClass
    lineage_refs: List[str] = Field(default_factory=list)

class RegrantRecord(BaseModel):
    id: str
    autonomy_id: str
    regrant_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class AutonomyDriftRecord(BaseModel):
    id: str
    autonomy_id: str
    drift_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ConfidenceMismatchRecord(BaseModel):
    id: str
    autonomy_id: str
    mismatch_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class BeneficiaryImpactRecord(BaseModel):
    id: str
    autonomy_id: str
    impact_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ShadowAutonomyRecord(BaseModel):
    id: str
    autonomy_id: str
    shadow_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class AutonomyComparisonRecord(BaseModel):
    id: str
    autonomy_id: str
    comparison_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class AutonomyObservationReport(BaseModel):
    id: str
    findings: List[str]

class AutonomyForecastReport(BaseModel):
    id: str
    forecasts: List[str]

class AutonomyDebtRecord(BaseModel):
    id: str
    autonomy_id: str
    debt_type: str
    severity: str
    lineage_refs: List[str] = Field(default_factory=list)

class AutonomyEquivalenceReport(BaseModel):
    id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str]

class AutonomyDivergenceReport(BaseModel):
    id: str
    divergences: List[str]

class AutonomyTrustVerdict(BaseModel):
    verdict: TrustVerdict
    factors: Dict[str, Any]

class AutonomyAuditRecord(BaseModel):
    id: str
    autonomy_id: str
    audit_notes: List[str]

class AutonomyArtifactManifest(BaseModel):
    id: str
    refs: List[str]
