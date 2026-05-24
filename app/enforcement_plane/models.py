from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.enforcement_plane.enums import (
    EnforcementClass, ReversibilityClass, AppealClass, DueProcessClass, TrustVerdictClass
)

class TriggerRecord(BaseModel):
    trigger_id: str
    basis: str
    evidence_ref: str
    is_authoritative: bool

class ScopeBoundRecord(BaseModel):
    actor_scope: Optional[str] = None
    tenant_scope: Optional[str] = None
    environment_scope: str = "PROD"
    beneficiary_impact: str

class AppealRecord(BaseModel):
    appeal_id: str
    status: str
    submitted_at: datetime
    resolved_at: Optional[datetime] = None

class LiftCriteriaRecord(BaseModel):
    criteria_id: str
    description: str
    is_met: bool = False
    residual_restriction_active: bool = False

class EnforcementObject(BaseModel):
    enforcement_id: str
    enforcement_class: EnforcementClass
    owner: str
    status: str = "ACTIVE"
    trigger: TriggerRecord
    scope: ScopeBoundRecord
    reversibility: ReversibilityClass
    due_process: DueProcessClass
    appeal_posture: AppealClass
    lift_criteria: Optional[LiftCriteriaRecord] = None
    expiry_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.now)

class EnforcementTrustVerdict(BaseModel):
    enforcement_id: str
    verdict: TrustVerdictClass
    factors: Dict[str, str]
    debt_warnings: List[str]
    blockers: List[str]
