from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.temporal_plane.enums import *

class ClockRecord(BaseModel):
    clock_id: str
    clock_class: ClockClass
    authority: str
    trust_notes: Optional[str] = None

class ClockAuthorityRecord(BaseModel):
    authority_id: str
    clock_ref: str
    is_authoritative: bool

class TimestampRecord(BaseModel):
    timestamp_id: str
    ts: datetime
    ts_class: TimestampClass
    confidence_notes: Optional[str] = None

class ValidityWindowRecord(BaseModel):
    window_id: str
    start_ts: datetime
    end_ts: Optional[datetime]
    window_class: WindowClass

class FreshnessRecord(BaseModel):
    posture: FreshnessClass
    evaluated_at: datetime

class AdmissibilityRecord(BaseModel):
    posture: AdmissibilityClass
    reason: str

class TemporalObject(BaseModel):
    temporal_id: str
    t_class: TemporalClass
    owner: str
    scope: str
    clock_authority: ClockAuthorityRecord
    validity: ValidityWindowRecord
    freshness: FreshnessRecord
    admissibility: AdmissibilityRecord

class TemporalObjectRef(BaseModel):
    temporal_id: str

class TemporalTrustVerdict(BaseModel):
    verdict: TrustVerdict
    reasons: List[str]

class TemporalArtifactManifest(BaseModel):
    manifest_id: str
    temporal_objects: List[TemporalObjectRef]
    verdict: TemporalTrustVerdict
