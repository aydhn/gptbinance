from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# TODO: Add specific enum imports


class PostmortemCourtConfig(BaseModel):
    enabled: bool = True
    require_chronology_verification: bool = True
    require_evidence_admissibility: bool = True


class PostmortemSeedRef(BaseModel):
    incident_id: str
    seed_timestamp: datetime
    affected_scopes: List[str]


class PostmortemScope(BaseModel):
    scopes: List[str]


class EvidenceAdmissibilityRecord(BaseModel):
    evidence_id: str
    is_admissible: bool
    reason: Optional[str] = None


class ChronologyEvent(BaseModel):
    timestamp: datetime
    event_type: str
    description: str


class ChronologyRecord(BaseModel):
    events: List[ChronologyEvent]
    is_verified: bool


class CausalNode(BaseModel):
    node_id: str
    description: str
    node_type: str


class CausalEdge(BaseModel):
    source_id: str
    target_id: str
    relationship: str


class CausalGraph(BaseModel):
    nodes: List[CausalNode]
    edges: List[CausalEdge]


class RootCauseCandidate(BaseModel):
    candidate_id: str
    description: str
    confidence: str


class ContributingFactor(BaseModel):
    factor_id: str
    description: str
    severity: str


class TriggerEvent(BaseModel):
    event_id: str
    description: str


class CounterfactualAssessment(BaseModel):
    scenario: str
    assessment: str


class CorrectiveAction(BaseModel):
    action_id: str
    description: str


class PreventiveAction(BaseModel):
    action_id: str
    description: str


class ActionTrackingRecord(BaseModel):
    action_id: str
    status: str


class RecurrenceRiskReport(BaseModel):
    score: float
    factors: List[str]


class LearningDebtRecord(BaseModel):
    debt_id: str
    description: str


class PostmortemVerdict(BaseModel):
    summary: str


class PostmortemAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime


class PostmortemArtifactManifest(BaseModel):
    artifacts: List[str]


class PostmortemRecord(BaseModel):
    postmortem_id: str
    seed_ref: PostmortemSeedRef
    verdict: PostmortemVerdict
