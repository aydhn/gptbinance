from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.representation_plane.enums import RepresentationClass, AudienceClass, MaterialityClass, RelianceClass, TrustVerdictEnum

class RepresentationObject(BaseModel):
    representation_id: str
    rep_class: RepresentationClass
    owner: str
    scope: str
    content: str
    audience: AudienceClass
    materiality: MaterialityClass
    reliance_posture: RelianceClass
    caveat_ids: List[str] = []
    disclaimer_ids: List[str] = []
    correction_ids: List[str] = []
    retraction_ids: List[str] = []
    evidence_refs: List[str] = []
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CaveatRecord(BaseModel):
    caveat_id: str
    representation_id: str
    content: str
    is_material: bool
    is_buried: bool = False

class DisclaimerRecord(BaseModel):
    disclaimer_id: str
    representation_id: str
    content: str
    limits_liability: bool
    is_laundering_attempt: bool = False

class CorrectionRecord(BaseModel):
    correction_id: str
    representation_id: str
    correction_content: str
    propagated_downstream: bool = False

class TrustVerdict(BaseModel):
    representation_id: str
    verdict: TrustVerdictEnum
    factors: Dict[str, str]
    blockers: List[str]
    warnings: List[str]
