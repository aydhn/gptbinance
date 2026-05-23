from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.liability_plane.enums import (
    LiabilityClass, ResponsibilityClass, CulpabilityClass, FaultClass,
    NegligenceClass, StrictLiabilityClass, CausationClass, ContributionClass,
    SharedLiabilityClass, JointLiabilityClass, SeveralLiabilityClass,
    IndemnityClass, ExonerationClass, LimitationClass, LiabilityCapClass,
    ConsequenceClass, CostBearerClass, DutyToMitigateClass, ResidualExposureClass,
    LiabilityState, EquivalenceVerdict, TrustVerdict
)

class LiabilityPlaneConfig(BaseModel):
    strict_mode: bool = True
    enforce_evidence: bool = True

class LiabilityObjectRef(BaseModel):
    liability_id: str
    liability_class: LiabilityClass

class ProofNote(BaseModel):
    note: str
    evidence_refs: List[str] = Field(default_factory=list)

class LiabilityObject(BaseModel):
    liability_id: str
    liability_class: LiabilityClass
    owner: str
    scope: str
    causation_posture: str
    exposure_posture: str
    state: LiabilityState = LiabilityState.ACTIVE
    created_at: datetime = Field(default_factory=datetime.now)

class CausationRecord(BaseModel):
    record_id: str
    liability_id: str
    causation_class: CausationClass
    actor: str
    description: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ContributionRecord(BaseModel):
    record_id: str
    liability_id: str
    contribution_class: ContributionClass
    actor: str
    percentage: float
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ResponsibilityRecord(BaseModel):
    record_id: str
    liability_id: str
    responsibility_class: ResponsibilityClass
    actor: str
    description: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class CulpabilityRecord(BaseModel):
    record_id: str
    liability_id: str
    culpability_class: CulpabilityClass
    actor: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class FaultRecord(BaseModel):
    record_id: str
    liability_id: str
    fault_class: FaultClass
    actor: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class NegligenceRecord(BaseModel):
    record_id: str
    liability_id: str
    negligence_class: NegligenceClass
    actor: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class StrictLiabilityRecord(BaseModel):
    record_id: str
    liability_id: str
    strict_liability_class: StrictLiabilityClass
    actor: str
    caveats: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class SharedLiabilityRecord(BaseModel):
    record_id: str
    liability_id: str
    shared_class: SharedLiabilityClass
    actors: List[str]
    allocations: Dict[str, float]
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class JointLiabilityRecord(BaseModel):
    record_id: str
    liability_id: str
    joint_class: JointLiabilityClass
    actors: List[str]
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class SeveralLiabilityRecord(BaseModel):
    record_id: str
    liability_id: str
    several_class: SeveralLiabilityClass
    actor: str
    exposure_amount: float
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnityRecord(BaseModel):
    record_id: str
    liability_id: str
    indemnity_class: IndemnityClass
    indemnifier: str
    indemnitee: str
    scope_description: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class RecourseAllocationRecord(BaseModel):
    record_id: str
    liability_id: str
    recourse_type: str
    target_actor: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ExonerationRecord(BaseModel):
    record_id: str
    liability_id: str
    exoneration_class: ExonerationClass
    actor: str
    basis: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class LimitationRecord(BaseModel):
    record_id: str
    liability_id: str
    limitation_class: LimitationClass
    description: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class LiabilityCapRecord(BaseModel):
    record_id: str
    liability_id: str
    cap_class: LiabilityCapClass
    amount: float
    currency: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ConsequenceAllocationRecord(BaseModel):
    record_id: str
    liability_id: str
    consequence_class: ConsequenceClass
    bearer: str
    description: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class CostBearerRecord(BaseModel):
    record_id: str
    liability_id: str
    bearer_class: CostBearerClass
    actor: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class DutyToMitigateRecord(BaseModel):
    record_id: str
    liability_id: str
    duty_class: DutyToMitigateClass
    actor: str
    status: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ResidualExposureRecord(BaseModel):
    record_id: str
    liability_id: str
    exposure_class: ResidualExposureClass
    actor: str
    description: str
    proof_notes: List[ProofNote] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class LiabilityComparisonRecord(BaseModel):
    comparison_id: str
    target_id: str
    comparison_type: str
    findings: List[str]
    lineage_refs: List[str] = Field(default_factory=list)

class LiabilityForecastReport(BaseModel):
    forecast_id: str
    liability_id: str
    exposure_growth_forecast: str
    indemnity_failure_risk: str
    uncertainty_class: str

class LiabilityDebtRecord(BaseModel):
    debt_id: str
    liability_id: str
    debt_type: str
    severity: str
    description: str

class LiabilityEquivalenceReport(BaseModel):
    report_id: str
    liability_id: str
    environments: List[str]
    verdict: EquivalenceVerdict
    divergence_notes: List[str]

class LiabilityDivergenceReport(BaseModel):
    report_id: str
    liability_id: str
    divergence_type: str
    severity: str
    blast_radius: str

class LiabilityTrustVerdict(BaseModel):
    verdict_id: str
    liability_id: str
    verdict: TrustVerdict
    causation_clarity_score: float
    allocation_rigor_score: float
    exoneration_honesty_score: float
    caveats: List[str]
    blockers: List[str]

class LiabilityReadinessBundle(BaseModel):
    bundle_id: str
    liability_id: str
    causation_clarity: bool
    allocation_rigor: bool
    indemnity_discipline: bool
    exoneration_honesty: bool
    exposure_visibility: bool
    proof_notes: List[ProofNote] = Field(default_factory=list)

class LiabilityAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    target_id: str
    timestamp: datetime = Field(default_factory=datetime.now)

class LiabilityArtifactManifest(BaseModel):
    manifest_id: str
    liability_id: str
    hashes: Dict[str, str]
    created_at: datetime = Field(default_factory=datetime.now)

class LiabilityRecord(BaseModel):
    liability: LiabilityObject
    responsibility: List[ResponsibilityRecord] = Field(default_factory=list)
    culpability: List[CulpabilityRecord] = Field(default_factory=list)
    fault: List[FaultRecord] = Field(default_factory=list)
    negligence: List[NegligenceRecord] = Field(default_factory=list)
    strict_liability: List[StrictLiabilityRecord] = Field(default_factory=list)
    causation: List[CausationRecord] = Field(default_factory=list)
    contribution: List[ContributionRecord] = Field(default_factory=list)
    shared: List[SharedLiabilityRecord] = Field(default_factory=list)
    joint: List[JointLiabilityRecord] = Field(default_factory=list)
    several: List[SeveralLiabilityRecord] = Field(default_factory=list)
    indemnity: List[IndemnityRecord] = Field(default_factory=list)
    recourse: List[RecourseAllocationRecord] = Field(default_factory=list)
    exoneration: List[ExonerationRecord] = Field(default_factory=list)
    limitation: List[LimitationRecord] = Field(default_factory=list)
    caps: List[LiabilityCapRecord] = Field(default_factory=list)
    consequences: List[ConsequenceAllocationRecord] = Field(default_factory=list)
    cost_bearers: List[CostBearerRecord] = Field(default_factory=list)
    mitigation_duties: List[DutyToMitigateRecord] = Field(default_factory=list)
    residual_exposure: List[ResidualExposureRecord] = Field(default_factory=list)
    trust_verdict: Optional[LiabilityTrustVerdict] = None
