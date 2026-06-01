from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.assurance_plane.enums import (
    AssuranceClass, ClaimClass, EvidenceClass, SufficiencyClass,
    CertificationClass, AttestationClass, SurveillanceClass,
    CaveatClass, RevocationClass, EquivalenceVerdict, TrustVerdict
)

class AssurancePlaneConfig(BaseModel):
    enforce_evidence_sufficiency: bool = True
    enforce_surveillance_rigor: bool = True
    block_caveat_suppression: bool = True

class AssuranceObjectRef(BaseModel):
    assurance_id: str
    class_type: AssuranceClass

class AssuranceObject(BaseModel):
    assurance_id: str
    class_type: AssuranceClass
    owner: str
    scope_refs: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AssuranceClaimRecord(BaseModel):
    claim_id: str
    assurance_id: str
    claim_class: ClaimClass
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class EvidenceItemRecord(BaseModel):
    item_id: str
    evidence_class: EvidenceClass
    source: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class EvidencePackRecord(BaseModel):
    pack_id: str
    items: List[EvidenceItemRecord]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SufficiencyRecord(BaseModel):
    sufficiency_id: str
    claim_id: str
    pack_id: str
    sufficiency_class: SufficiencyClass
    evaluation_notes: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AssuranceCaseRecord(BaseModel):
    case_id: str
    assurance_id: str
    claims: List[AssuranceClaimRecord]
    packs: List[EvidencePackRecord]
    sufficiencies: List[SufficiencyRecord]
    is_complete: bool

class CertificationRecord(BaseModel):
    certification_id: str
    assurance_id: str
    certification_class: CertificationClass
    issuer: str
    valid_until: Optional[datetime]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AttestationRecord(BaseModel):
    attestation_id: str
    assurance_id: str
    attestation_class: AttestationClass
    attestor: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SurveillanceFindingRecord(BaseModel):
    finding_id: str
    assurance_id: str
    finding_type: str
    is_clean: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SurveillanceCycleRecord(BaseModel):
    cycle_id: str
    assurance_id: str
    surveillance_class: SurveillanceClass
    findings: List[SurveillanceFindingRecord]
    next_check: Optional[datetime]

class CaveatRecord(BaseModel):
    caveat_id: str
    assurance_id: str
    caveat_class: CaveatClass
    description: str

class ContradictionRecord(BaseModel):
    contradiction_id: str
    assurance_id: str
    description: str
    is_material: bool
    is_resolved: bool

class ExpiryRecord(BaseModel):
    expiry_id: str
    assurance_id: str
    is_expired: bool
    reason: str

class RevocationTriggerRecord(BaseModel):
    trigger_id: str
    assurance_id: str
    revocation_class: RevocationClass
    conditions: str

class DowngradeRecord(BaseModel):
    downgrade_id: str
    assurance_id: str
    reason: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class IndependentReviewRecord(BaseModel):
    review_id: str
    assurance_id: str
    reviewer: str
    is_clean: bool
    notes: str

class AssuranceScopeRecord(BaseModel):
    scope_id: str
    assurance_id: str
    boundaries: str

class AssuranceRecord(BaseModel):
    record_id: str
    assurance_obj: AssuranceObject
    cases: List[AssuranceCaseRecord]
    certifications: List[CertificationRecord]
    attestations: List[AttestationRecord]
    surveillance: List[SurveillanceCycleRecord]
    caveats: List[CaveatRecord]
    contradictions: List[ContradictionRecord]
    expiry: Optional[ExpiryRecord] = None
    revocations: List[RevocationTriggerRecord]

class AssuranceTrustVerdict(BaseModel):
    verdict_id: str
    assurance_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AssuranceComparisonRecord(BaseModel):
    comparison_id: str
    source_assurance_id: str
    target_assurance_id: str
    notes: str

class AssuranceForecastReport(BaseModel):
    forecast_id: str
    expiry_risk: str
    contradiction_emergence: str
    surveillance_decay: str

class AssuranceDebtRecord(BaseModel):
    debt_id: str
    assurance_id: str
    debt_type: str
    severity: str

class AssuranceEquivalenceReport(BaseModel):
    report_id: str
    source_env: str
    target_env: str
    verdict: EquivalenceVerdict
    divergence_notes: str

class AssuranceDivergenceReport(BaseModel):
    report_id: str
    assurance_id: str
    severity: str
    details: str

class AssuranceObservationReport(BaseModel):
    report_id: str
    assurance_id: str
    details: str

class AssuranceAuditRecord(BaseModel):
    audit_id: str
    assurance_id: str
    action: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AssuranceArtifactManifest(BaseModel):
    manifest_id: str
    assurance_id: str
    hash_refs: Dict[str, str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
