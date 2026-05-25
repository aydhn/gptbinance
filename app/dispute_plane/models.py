from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from .enums import *

class DisputeObjectRef(BaseModel):
    dispute_id: str
    target_id: str
    relation: str

class ComplaintRecord(BaseModel):
    complaint_id: str
    complaint_class: ComplaintClass
    description: str
    is_admitted: bool = False

class ClaimRecord(BaseModel):
    claim_id: str
    claim_class: ClaimClass
    basis: str

class IssueRecord(BaseModel):
    issue_id: str
    issue_class: IssueClass
    description: str
    resolved: bool = False

class BurdenRecord(BaseModel):
    burden_id: str
    burden_class: BurdenClass
    assigned_to: str

class HearingRecord(BaseModel):
    hearing_id: str
    is_formal: bool
    record_complete: bool

class RulingRecord(BaseModel):
    ruling_id: str
    ruling_class: RulingClass
    rationale: str
    on_record: bool

class AppealRecord(BaseModel):
    appeal_id: str
    appeal_class: AppealClass
    stays_enforcement: bool

class DismissalRecord(BaseModel):
    dismissal_id: str
    reason: str
    with_prejudice: bool

class SettlementUnderDisputeRecord(BaseModel):
    settlement_id: str
    surviving_issues: List[str]

class DisputeRecord(BaseModel):
    dispute_id: str
    dispute_class: DisputeClass
    owner: str
    scope: str
    complaints: List[ComplaintRecord] = []
    claims: List[ClaimRecord] = []
    issues: List[IssueRecord] = []
    burdens: List[BurdenRecord] = []
    hearings: List[HearingRecord] = []
    rulings: List[RulingRecord] = []
    appeals: List[AppealRecord] = []
    dismissals: List[DismissalRecord] = []
    settlements: List[SettlementUnderDisputeRecord] = []
    disposition_posture: Optional[DispositionClass] = None

class DisputeTrustVerdictRecord(BaseModel):
    verdict: DisputeTrustVerdict
    factors: Dict[str, Any]
    blockers: List[str]
    cautions: List[str]
