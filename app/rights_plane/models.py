from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.rights_plane.enums import (
    RightClass, EntitlementClass, ClaimClass, StandingClass,
    ConsentClass, WaiverClass, RevocationClass, BeneficiaryClass,
    ExhaustionClass, EquivalenceVerdict, TrustVerdict
)

class RightsPlaneConfig(BaseModel):
    strict_mode: bool = True

class RightsObjectRef(BaseModel):
    ref_id: str
    ref_type: str

class RightsObject(BaseModel):
    rights_id: str
    object_class: str
    owner: str
    scope: str
    beneficiary_posture: str
    enforceability_posture: str

class BeneficiaryRecord(BaseModel):
    beneficiary_id: str
    beneficiary_class: BeneficiaryClass
    scope: str
    is_federated: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class HolderRecord(BaseModel):
    holder_id: str
    holder_type: str
    beneficiary_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class RepresentativeRecord(BaseModel):
    representative_id: str
    representative_type: str
    holder_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class RightRecord(BaseModel):
    right_id: str
    right_class: RightClass
    holder_id: str
    is_inalienable: bool = False
    is_exhausted: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class EntitlementRecord(BaseModel):
    entitlement_id: str
    entitlement_class: EntitlementClass
    right_ref: str
    conditions: Dict[str, Any] = Field(default_factory=dict)
    lineage_refs: List[str] = Field(default_factory=list)

class ClaimRecord(BaseModel):
    claim_id: str
    claim_class: ClaimClass
    right_ref: str
    standing_class: StandingClass
    lineage_refs: List[str] = Field(default_factory=list)

class DelegatedClaimRecord(BaseModel):
    delegated_claim_id: str
    claim_ref: str
    representative_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class StandingRecord(BaseModel):
    standing_id: str
    standing_class: StandingClass
    beneficiary_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class ConsentScopeRecord(BaseModel):
    scope_id: str
    purpose: str
    duration: str
    is_blanket: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class ConsentRecord(BaseModel):
    consent_id: str
    holder_ref: str
    scope_ref: str
    consent_class: ConsentClass
    lineage_refs: List[str] = Field(default_factory=list)

class WithdrawalRecord(BaseModel):
    withdrawal_id: str
    consent_ref: str
    status: str
    lineage_refs: List[str] = Field(default_factory=list)

class RevocationRecord(BaseModel):
    revocation_id: str
    revocation_class: RevocationClass
    right_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class WaiverRecord(BaseModel):
    waiver_id: str
    waiver_class: WaiverClass
    right_ref: str
    representative_id: Optional[str]
    lineage_refs: List[str] = Field(default_factory=list)

class InalienableRightRecord(BaseModel):
    inalienable_id: str
    right_ref: str
    protection_level: str
    lineage_refs: List[str] = Field(default_factory=list)

class AccessRightRecord(BaseModel):
    access_id: str
    right_ref: str
    access_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class UseRightRecord(BaseModel):
    use_id: str
    right_ref: str
    use_bounds: str
    lineage_refs: List[str] = Field(default_factory=list)

class NoticeRightRecord(BaseModel):
    notice_id: str
    right_ref: str
    notice_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class RemedyRightRecord(BaseModel):
    remedy_id: str
    right_ref: str
    remedy_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ChallengeRightRecord(BaseModel):
    challenge_id: str
    right_ref: str
    challenge_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class PortabilityRightRecord(BaseModel):
    portability_id: str
    right_ref: str
    portability_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ExhaustionRecord(BaseModel):
    exhaustion_id: str
    exhaustion_class: ExhaustionClass
    right_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class SurvivalRecord(BaseModel):
    survival_id: str
    right_ref: str
    survival_reason: str
    lineage_refs: List[str] = Field(default_factory=list)

class RightsConflictRecord(BaseModel):
    conflict_id: str
    right_refs: List[str]
    conflict_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class RightsComparisonRecord(BaseModel):
    comparison_id: str
    item_a: str
    item_b: str
    comparison_result: str
    lineage_refs: List[str] = Field(default_factory=list)

class RightsObservationReport(BaseModel):
    report_id: str
    observations: Dict[str, Any]

class RightsForecastReport(BaseModel):
    forecast_id: str
    forecasts: Dict[str, Any]

class RightsDebtRecord(BaseModel):
    debt_id: str
    debt_type: str
    severity: str

class RightsEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    divergence_refs: List[str]

class RightsDivergenceReport(BaseModel):
    report_id: str
    divergences: List[Dict[str, Any]]

class RightsTrustVerdict(BaseModel):
    verdict: TrustVerdict
    cautions: List[str]
    blockers: List[str]

class RightsAuditRecord(BaseModel):
    audit_id: str
    action: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class RightsArtifactManifest(BaseModel):
    manifest_id: str
    artifacts: List[str]
