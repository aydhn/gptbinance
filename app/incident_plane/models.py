from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.incident_plane.enums import IncidentSeverity, IncidentUrgency, IncidentStatus, VerificationVerdict

class IncidentSignal(BaseModel):
    signal_id: str
    source_system: str
    raw_payload: Dict[str, Any]
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    confidence_score: float

class IncidentTriageRecord(BaseModel):
    incident_id: str
    provisional_facts: List[str]
    hypotheses: List[str]
    missing_information_blockers: List[str]
    proof_notes: str
    triaged_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    triaged_by: str

class RecoveryVerificationRecord(BaseModel):
    incident_id: str
    objective_checks_passed: bool
    no_regression_checks_passed: bool
    quiet_period_met: bool
    residual_risk_assessment: str
    verdict: VerificationVerdict
    verified_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    verified_by: str
    proof_notes: str

class IncidentStatusEvent(BaseModel):
    incident_id: str
    previous_status: Optional[IncidentStatus]
    new_status: IncidentStatus
    reason: str
    transitioned_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    transitioned_by: str

class IncidentManifest(BaseModel):
    incident_id: str
    family: str
    severity: IncidentSeverity
    urgency: IncidentUrgency
    current_status: IncidentStatus
    blast_radius: Dict[str, Any]
    primary_owner: str
    signals: List[IncidentSignal] = Field(default_factory=list)
    triage: Optional[IncidentTriageRecord] = None
    timeline: List[IncidentStatusEvent] = Field(default_factory=list)
    verification: Optional[RecoveryVerificationRecord] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
