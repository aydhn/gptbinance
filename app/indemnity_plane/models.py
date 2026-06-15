from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from app.indemnity_plane.enums import (
    IndemnityClass, LossClass, IndemnitorClass, CoverageClass, ExclusionClass,
    DefenseClass, ReimbursementClass, NoticeClass, DebtClass, EquivalenceVerdict, TrustVerdict
)

class IndemnityPlaneConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True

class IndemnityObjectRef(BaseModel):
    indemnity_id: str
    owner: str
    scope: str
    class_type: str = "indemnity_object"

class IndemnityObject(BaseModel):
    id: str
    class_type: IndemnityClass
    owner: str
    scope: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class IndemnityRecord(BaseModel):
    indemnity_id: str
    state: str
    proof_notes: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnifiedSubjectRecord(BaseModel):
    indemnity_id: str
    subject_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnifiedClaimRecord(BaseModel):
    indemnity_id: str
    claim_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class CoveredLossRecord(BaseModel):
    indemnity_id: str
    loss_class: LossClass
    amount: Optional[float] = None
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnitorRecord(BaseModel):
    indemnity_id: str
    indemnitor_class: IndemnitorClass
    identity: str
    lineage_refs: List[str] = Field(default_factory=list)

class IndemniteeRecord(BaseModel):
    indemnity_id: str
    identity: str
    is_beneficiary: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnityBasisRecord(BaseModel):
    indemnity_id: str
    is_sufficient: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class CoverageRecord(BaseModel):
    indemnity_id: str
    coverage_class: CoverageClass
    lineage_refs: List[str] = Field(default_factory=list)

class ExclusionRecord(BaseModel):
    indemnity_id: str
    exclusion_class: ExclusionClass
    lineage_refs: List[str] = Field(default_factory=list)

class CarveOutRecord(BaseModel):
    indemnity_id: str
    is_clear: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class NoticeRecord(BaseModel):
    indemnity_id: str
    notice_class: NoticeClass
    lineage_refs: List[str] = Field(default_factory=list)

class NoticeTimingRecord(BaseModel):
    indemnity_id: str
    is_timely: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class PrejudiceRecord(BaseModel):
    indemnity_id: str
    has_prejudice: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class CooperationRecord(BaseModel):
    indemnity_id: str
    is_valid: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class DefenseDutyRecord(BaseModel):
    indemnity_id: str
    defense_class: DefenseClass
    lineage_refs: List[str] = Field(default_factory=list)

class DefenseControlRecord(BaseModel):
    indemnity_id: str
    is_clean: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class AdvancementRecord(BaseModel):
    indemnity_id: str
    is_valid: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class ReimbursementRecord(BaseModel):
    indemnity_id: str
    reimbursement_class: ReimbursementClass
    lineage_refs: List[str] = Field(default_factory=list)

class ReimbursementDelayRecord(BaseModel):
    indemnity_id: str
    has_delay: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class SettlementConsentRecord(BaseModel):
    indemnity_id: str
    consent_granted: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class ConsentConflictRecord(BaseModel):
    indemnity_id: str
    has_conflict: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class CapRecord(BaseModel):
    indemnity_id: str
    is_bounded: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class BasketRecord(BaseModel):
    indemnity_id: str
    has_basket: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class DeductibleRecord(BaseModel):
    indemnity_id: str
    has_deductible: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class AntiDuplicationRecord(BaseModel):
    indemnity_id: str
    is_clean: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class SubrogationRecord(BaseModel):
    indemnity_id: str
    is_valid: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class RecoupmentRecord(BaseModel):
    indemnity_id: str
    is_valid: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class PartialIndemnityRecord(BaseModel):
    indemnity_id: str
    is_bounded: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class FailedIndemnityRecord(BaseModel):
    indemnity_id: str
    has_failure: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class IllusoryIndemnityRecord(BaseModel):
    indemnity_id: str
    has_illusory_risk: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnityDebtRecord(BaseModel):
    indemnity_id: str
    debt_class: DebtClass
    severity: str
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnityDriftRecord(BaseModel):
    indemnity_id: str
    drift_factor: str
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnityComparisonRecord(BaseModel):
    comparison_type: str
    is_comparable: bool = True
    lineage_refs: List[str] = Field(default_factory=list)

class IndemnityObservationReport(BaseModel):
    report_id: str
    observations: List[Dict[str, Any]]

class IndemnityForecastReport(BaseModel):
    report_id: str
    forecasts: List[Dict[str, Any]]

class IndemnityEquivalenceReport(BaseModel):
    verdict: EquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)
    proof_notes: List[str] = Field(default_factory=list)

class IndemnityDivergenceReport(BaseModel):
    divergence_type: str
    severity: str

class IndemnityTrustVerdict(BaseModel):
    indemnity_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any] = Field(default_factory=dict)
    proof_notes: List[str] = Field(default_factory=list)

class IndemnityAuditRecord(BaseModel):
    indemnity_id: str
    audit_notes: List[str] = Field(default_factory=list)

class IndemnityArtifactManifest(BaseModel):
    manifest_id: str
    indemnity_refs: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)
