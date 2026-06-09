from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.investigation_plane.enums import (
    InvestigationClass, AllegationClass, IntakeClass, TriageClass,
    ScopeClass, EvidenceClass, CustodyClass, InterviewClass,
    SubstantiationClass, DebtClass, TrustVerdict
)

class InvestigationObject(BaseModel):
    investigation_id: str
    investigation_class: InvestigationClass
    owner: str
    status: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class InvestigationRecord(BaseModel):
    record_id: str
    investigation_id: str
    state: str
    notes: Optional[str]

class AllegationRecord(BaseModel):
    allegation_id: str
    investigation_id: str
    allegation_class: AllegationClass
    description: str

class ReporterRecord(BaseModel):
    reporter_id: str
    investigation_id: str
    reporter_type: str

class AffectedPartyRecord(BaseModel):
    party_id: str
    investigation_id: str
    party_type: str

class IntakeRecord(BaseModel):
    intake_id: str
    investigation_id: str
    intake_class: IntakeClass

class TriageRecord(BaseModel):
    triage_id: str
    investigation_id: str
    triage_class: TriageClass

class InquiryThresholdRecord(BaseModel):
    threshold_id: str
    investigation_id: str
    status: str

class ScopeHypothesisRecord(BaseModel):
    hypothesis_id: str
    investigation_id: str
    scope_class: ScopeClass

class ScopeControlRecord(BaseModel):
    control_id: str
    investigation_id: str
    status: str

class PreservationHoldRecord(BaseModel):
    hold_id: str
    investigation_id: str
    status: str

class EvidenceRecord(BaseModel):
    evidence_id: str
    investigation_id: str
    evidence_class: EvidenceClass

class EvidenceSourceRecord(BaseModel):
    source_id: str
    evidence_id: str
    reliability: str

class EvidenceIntegrityRecord(BaseModel):
    integrity_id: str
    evidence_id: str
    status: str

class ChainOfCustodyRecord(BaseModel):
    custody_id: str
    evidence_id: str
    custody_class: CustodyClass

class CorroborationRecord(BaseModel):
    corroboration_id: str
    evidence_id: str
    status: str

class WitnessRecord(BaseModel):
    witness_id: str
    investigation_id: str
    witness_type: str

class InterviewRecord(BaseModel):
    interview_id: str
    witness_id: str
    interview_class: InterviewClass

class InterviewFairnessRecord(BaseModel):
    fairness_id: str
    interview_id: str
    posture: str

class ConflictScreenRecord(BaseModel):
    screen_id: str
    investigation_id: str
    status: str

class ContaminationRiskRecord(BaseModel):
    risk_id: str
    investigation_id: str
    level: str

class SpoliationRiskRecord(BaseModel):
    risk_id: str
    investigation_id: str
    level: str

class ExculpatoryEvidenceRecord(BaseModel):
    exculpatory_id: str
    investigation_id: str
    status: str

class SubstantiationRecord(BaseModel):
    substantiation_id: str
    investigation_id: str
    substantiation_class: SubstantiationClass

class ReferralRecord(BaseModel):
    referral_id: str
    investigation_id: str
    status: str

class InvestigativeGapRecord(BaseModel):
    gap_id: str
    investigation_id: str
    severity: str

class InvestigationDebtRecord(BaseModel):
    debt_id: str
    investigation_id: str
    debt_class: DebtClass
    interest: str

class InvestigationTrustVerdict(BaseModel):
    verdict_id: str
    investigation_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any]
