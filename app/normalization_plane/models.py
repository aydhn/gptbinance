from datetime import timezone

from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.normalization_plane.enums import (
    NormalizationClass, ReentryGateStatus, AuthorizationClass,
    GuardrailClass, LimitLiftClass, ResidualScarClass, NormalizationTrustVerdict
)

class NormalizationObjectRef(BaseModel):
    normalization_id: str
    version: str

class ResidualScarRecord(BaseModel):
    scar_id: str
    scar_class: ResidualScarClass
    description: str
    domain: str
    is_hidden: bool = False

class GuardrailRecord(BaseModel):
    guardrail_id: str
    guardrail_class: GuardrailClass
    description: str
    is_active: bool

class LimitLiftRecord(BaseModel):
    lift_id: str
    lift_class: LimitLiftClass
    domain: str
    is_premature: bool

class ReentryGateRecord(BaseModel):
    gate_id: str
    status: ReentryGateStatus
    notes: str

class NormalizationRecord(BaseModel):
    normalization_id: str
    normalization_class: NormalizationClass
    owner: str
    domain: str
    reentry_gate: Optional[ReentryGateRecord]
    guardrails: List[GuardrailRecord] = []
    limit_lifts: List[LimitLiftRecord] = []
    residual_scars: List[ResidualScarRecord] = []
    proof_notes: str = ""
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class NormalizationTrustReport(BaseModel):
    verdict: NormalizationTrustVerdict
    reentry_clarity: str
    authorization_rigor: str
    guardrail_integrity: str
    residual_scar_visibility: str
    blockers: List[str] = []
    cautions: List[str] = []
