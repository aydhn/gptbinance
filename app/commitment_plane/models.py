from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.commitment_plane.enums import (
    CommitmentClass, PromiseClass, ObligationClass, GuaranteeClass,
    BindingClass, OwnerClass, BreachClass, ReliefClass, DischargeClass,
    AsymmetryClass, CommitmentEquivalenceVerdict, CommitmentTrustVerdict
)

class CommitmentObjectRef(BaseModel):
    commitment_id: str
    version: str = "v1"

class BindingStrengthRecord(BaseModel):
    binding_class: BindingClass
    notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class OwnerRecord(BaseModel):
    owner_id: str
    owner_class: OwnerClass
    clarity_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class AccountabilityRecord(BaseModel):
    accountable_actor: str
    execution_actor: Optional[str] = None
    escalation_actor: Optional[str] = None
    breach_responder: Optional[str] = None
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ConditionRecord(BaseModel):
    condition_type: str # 'activation', 'discharge', 'relief', 'invalidation'
    description: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TriggerRecord(BaseModel):
    trigger_type: str # 'incident', 'release', 'contract', 'policy'
    description: str
    ambiguity_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class DeadlineRecord(BaseModel):
    deadline_type: str # 'hard', 'soft', 'customer', 'regulatory'
    timestamp: datetime
    breach_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class BreachRecord(BaseModel):
    breach_class: BreachClass
    description: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ReliefRecord(BaseModel):
    relief_class: ReliefClass
    description: str
    abuse_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class CompensatingObligationRecord(BaseModel):
    obligation_type: str # 'delivery', 'review', 'reporting', 'control'
    description: str
    sufficiency_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class DischargeRecord(BaseModel):
    discharge_class: DischargeClass
    description: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class RetirementRecord(BaseModel):
    retirement_type: str # 'retired', 'superseded', 'obsolete'
    description: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class AsymmetryRecord(BaseModel):
    asymmetry_class: AsymmetryClass
    description: str
    burden_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class PromiseRecord(BaseModel):
    promise_class: PromiseClass
    description: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ObligationRecord(BaseModel):
    obligation_class: ObligationClass
    description: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class GuaranteeRecord(BaseModel):
    guarantee_class: GuaranteeClass
    description: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TargetRecord(BaseModel):
    target_type: str # 'performance', 'delivery', 'risk_reduction', 'learning'
    description: str
    warnings: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ExpectationRecord(BaseModel):
    expectation_type: str # 'soft', 'stakeholder', 'inferred'
    description: str
    ambiguity_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class AspirationRecord(BaseModel):
    aspiration_type: str # 'strategic', 'capability', 'maturity'
    description: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class CommitmentObject(BaseModel):
    commitment_id: str
    commitment_class: CommitmentClass
    scope: str
    description: str
    binding: BindingStrengthRecord
    owners: List[OwnerRecord]
    accountability: AccountabilityRecord
    deadlines: List[DeadlineRecord] = Field(default_factory=list)
    conditions: List[ConditionRecord] = Field(default_factory=list)
    triggers: List[TriggerRecord] = Field(default_factory=list)
    breaches: List[BreachRecord] = Field(default_factory=list)
    reliefs: List[ReliefRecord] = Field(default_factory=list)
    compensating_obligations: List[CompensatingObligationRecord] = Field(default_factory=list)
    discharges: List[DischargeRecord] = Field(default_factory=list)
    retirements: List[RetirementRecord] = Field(default_factory=list)
    asymmetries: List[AsymmetryRecord] = Field(default_factory=list)

    # Specifics
    promise_details: Optional[PromiseRecord] = None
    obligation_details: Optional[ObligationRecord] = None
    guarantee_details: Optional[GuaranteeRecord] = None
    target_details: Optional[TargetRecord] = None
    expectation_details: Optional[ExpectationRecord] = None
    aspiration_details: Optional[AspirationRecord] = None

class CommitmentRecord(BaseModel):
    commitment: CommitmentObject
    status: str # 'active', 'pending', 'discharged', 'breached'
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class CommitmentComparisonRecord(BaseModel):
    comparison_type: str # 'promised_vs_delivered', 'internal_vs_external', 'committed_vs_aspirational'
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class CommitmentObservationReport(BaseModel):
    timestamp: datetime
    events: List[Dict[str, Any]]

class CommitmentForecastReport(BaseModel):
    forecast_type: str # 'breach_likelihood', 'owner_overload', 'deadline_slip', 'relief_overuse', 'asymmetry_growth'
    description: str
    uncertainty_class: str

class CommitmentDebtRecord(BaseModel):
    debt_type: str # 'ownerless', 'silent_extension', 'weak_backing', 'relief_abuse', 'breached_undischarged'
    severity: str
    interest: str

class CommitmentEquivalenceReport(BaseModel):
    verdict: CommitmentEquivalenceVerdict
    blockers: List[str] = Field(default_factory=list)

class CommitmentDivergenceReport(BaseModel):
    divergence_type: str # 'binding', 'owner', 'deadline', 'breach_discharge', 'asymmetry'
    severity: str
    blast_radius: str

class CommitmentTrustVerdictModel(BaseModel):
    verdict: CommitmentTrustVerdict
    factors: Dict[str, str]
    breakdown: Dict[str, Any]

class CommitmentAuditRecord(BaseModel):
    timestamp: datetime
    action: str
    actor: str
    commitment_id: str

class CommitmentArtifactManifest(BaseModel):
    manifest_id: str
    commitments: List[CommitmentObjectRef]
    hashes: Dict[str, str]

class CommitmentPlaneConfig(BaseModel):
    registry_mode: str = "strict"
