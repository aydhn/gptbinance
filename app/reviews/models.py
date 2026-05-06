from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.reviews.enums import (
    ReviewClass,
    QueueClass,
    ReviewPriority,
    SLASeverity,
    AssignmentClass,
    ChecklistVerdict,
    AdjudicationVerdict,
    EscalationClass,
    HandoffClass,
    ReviewState,
)


class ReviewScope(BaseModel):
    workspace_id: Optional[str] = None
    profile_id: Optional[str] = None
    symbol: Optional[str] = None
    session_id: Optional[str] = None
    candidate_id: Optional[str] = None
    incident_id: Optional[str] = None
    postmortem_id: Optional[str] = None
    release_id: Optional[str] = None
    migration_id: Optional[str] = None
    narrow_explicitly: bool = False


class ReviewRequestRef(BaseModel):
    source_artefact_id: str
    source_type: str


class ReviewRequest(BaseModel):
    request_id: str
    review_class: ReviewClass
    scope: ReviewScope
    priority_hint: ReviewPriority = ReviewPriority.MEDIUM
    rationale: str
    refs: List[ReviewRequestRef] = Field(default_factory=list)
    is_high_risk: bool = False
    requires_dual_control: bool = False
    producer_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewQueue(BaseModel):
    queue_id: str
    queue_class: QueueClass
    name: str
    description: str


class QueueItem(BaseModel):
    item_id: str
    queue_id: str
    request: ReviewRequest
    priority: ReviewPriority
    state: ReviewState = ReviewState.PENDING
    queued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewSLA(BaseModel):
    review_class: ReviewClass
    severity: SLASeverity
    response_timeout_minutes: int
    completion_timeout_minutes: int


class ReviewAssignment(BaseModel):
    assignment_id: str
    item_id: str
    assignee_id: str
    assignment_class: AssignmentClass
    assigned_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: bool = True


class ChecklistItem(BaseModel):
    item_id: str
    description: str
    is_required: bool = True
    verdict: ChecklistVerdict = ChecklistVerdict.INCOMPLETE
    completed_by: Optional[str] = None
    completed_at: Optional[datetime] = None
    notes: Optional[str] = None


class ReviewChecklist(BaseModel):
    checklist_id: str
    item_id: str
    items: List[ChecklistItem] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewEvidencePackRef(BaseModel):
    evidence_id: str
    is_redacted: bool = False
    notes: Optional[str] = None


class ReviewSession(BaseModel):
    session_id: str
    item_id: str
    assignments: List[ReviewAssignment] = Field(default_factory=list)
    checklist: Optional[ReviewChecklist] = None
    evidence_refs: List[ReviewEvidencePackRef] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewAdjudication(BaseModel):
    adjudication_id: str
    item_id: str
    adjudicator_id: str
    verdict: AdjudicationVerdict
    rationale: str
    conditions: Optional[str] = None
    adjudicated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewDecisionRecord(BaseModel):
    decision_id: str
    adjudication: ReviewAdjudication
    accepted_constraints: List[str] = Field(default_factory=list)
    rejected_evidence: List[str] = Field(default_factory=list)
    expiry: Optional[datetime] = None
    downstream_effects: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewEscalation(BaseModel):
    escalation_id: str
    item_id: str
    escalation_class: EscalationClass
    reason: str
    escalated_by: str
    escalated_to_role: str
    escalated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewHandoff(BaseModel):
    handoff_id: str
    item_id: str
    handoff_class: HandoffClass
    from_assignee_id: str
    to_assignee_id: str
    reason: str
    handoff_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SeparationOfDutiesCheck(BaseModel):
    item_id: str
    producer_id: str
    adjudicator_id: str
    is_valid: bool
    reason: str


class ReviewHistoryRecord(BaseModel):
    record_id: str
    item_id: str
    event_type: str
    actor_id: str
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewAuditRecord(BaseModel):
    audit_id: str
    item_id: str
    request: ReviewRequest
    decision: Optional[ReviewDecisionRecord] = None
    history: List[ReviewHistoryRecord] = Field(default_factory=list)
    archived_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewArtifactManifest(BaseModel):
    manifest_id: str
    item_id: str
    artefact_refs: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewFabricConfig(BaseModel):
    enabled: bool = True
    require_dual_control_for_high_risk: bool = True
    default_sla_response_minutes: int = 60
    default_sla_completion_minutes: int = 24 * 60
