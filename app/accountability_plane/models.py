from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime
from app.accountability_plane.enums import (
    AccountabilityClass, SubjectClass, DutyClass, BreachClass,
    EscalationClass, SanctionClass, RemediationClass, AppealClass,
    ReinstatementClass, EquivalenceVerdict, TrustVerdict
)

class AccountabilityPlaneConfig(BaseModel):
    strict_mode: bool = True

class AccountableSubjectRecord(BaseModel):
    subject_id: str
    subject_class: SubjectClass
    metadata: Dict = Field(default_factory=dict)
    lineage_refs: List[str] = Field(default_factory=list)

class RoleRecord(BaseModel):
    role_id: str
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class DutySourceRecord(BaseModel):
    source_id: str
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class DutyRecord(BaseModel):
    duty_id: str
    duty_class: DutyClass
    subject_ref: str
    source_ref: Optional[str] = None
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class NonDelegableDutyRecord(DutyRecord):
    is_hard: bool = True

class DelegatedDutyRecord(DutyRecord):
    delegated_to: str
    is_valid: bool = True

class BreachRecord(BaseModel):
    breach_id: str
    breach_class: BreachClass
    duty_ref: str
    evidence_refs: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class OmissionRecord(BaseModel):
    omission_id: str
    omission_type: str
    duty_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class EscalationFailureRecord(BaseModel):
    escalation_id: str
    escalation_class: EscalationClass
    breach_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class SharedAccountabilityRecord(BaseModel):
    shared_id: str
    subject_refs: List[str]
    is_legitimate: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class ScapegoatingRiskRecord(BaseModel):
    risk_id: str
    description: str
    breach_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class SanctionTierRecord(BaseModel):
    tier_id: str
    sanction_class: SanctionClass
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class SanctionRecord(BaseModel):
    sanction_id: str
    tier_ref: str
    breach_ref: str
    subject_ref: str
    is_symbolic: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class RemediationBurdenRecord(BaseModel):
    remediation_id: str
    remediation_class: RemediationClass
    breach_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class RestitutionBurdenRecord(BaseModel):
    restitution_id: str
    breach_ref: str
    is_resolved: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class DisqualificationRecord(BaseModel):
    disqualification_id: str
    subject_ref: str
    is_temporary: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class AppealRecord(BaseModel):
    appeal_id: str
    appeal_class: AppealClass
    sanction_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class ReversalRecord(BaseModel):
    reversal_id: str
    appeal_ref: str
    is_full: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class ReinstatementRecord(BaseModel):
    reinstatement_id: str
    reinstatement_class: ReinstatementClass
    subject_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class AccountabilityObjectRef(BaseModel):
    ref_id: str
    acc_class: AccountabilityClass

class AccountabilityObject(BaseModel):
    accountability_id: str
    acc_class: AccountabilityClass
    owner: str = "system"
    scope: str = "global"
    duty_posture: str = "unknown"
    consequence_posture: str = "unknown"
    subject_refs: List[str] = Field(default_factory=list)
    duty_refs: List[str] = Field(default_factory=list)
    breach_refs: List[str] = Field(default_factory=list)
    sanction_refs: List[str] = Field(default_factory=list)
    restitution_refs: List[str] = Field(default_factory=list)
    is_closed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    lineage_refs: List[str] = Field(default_factory=list)

class AccountabilityRecord(BaseModel):
    acc_obj: AccountabilityObject
    status: str = "open"

class AccountabilityComparisonRecord(BaseModel):
    compare_id: str
    description: str

class AccountabilityObservationReport(BaseModel):
    report_id: str
    observations: List[str]

class AccountabilityForecastReport(BaseModel):
    forecast_id: str
    predictions: List[str]

class AccountabilityDebtRecord(BaseModel):
    debt_id: str
    severity: str
    description: str

class AccountabilityEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict

class AccountabilityDivergenceReport(BaseModel):
    report_id: str
    divergences: List[str]

class AccountabilityTrustVerdict(BaseModel):
    verdict: TrustVerdict
    factors: Dict[str, str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AccountabilityAuditRecord(BaseModel):
    audit_id: str
    findings: List[str]

class AccountabilityArtifactManifest(BaseModel):
    manifest_id: str
    hashes: Dict[str, str]
