from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from app.policy_plane.enums import (
    PolicyClass,
    RuleClass,
    InvariantClass,
    ObligationClass,
    SubjectClass,
    ActionClass,
    ResourceClass,
    VerdictClass,
    ExceptionClass,
    EquivalenceVerdict,
    TrustVerdict,
    ConflictSeverity,
)


def utcnow():
    return datetime.now(timezone.utc)


class PolicySubject(BaseModel):
    subject_class: SubjectClass
    subject_id: str


class PolicyAction(BaseModel):
    action_class: ActionClass
    action_id: Optional[str] = None


class PolicyResource(BaseModel):
    resource_class: ResourceClass
    resource_id: str


class PolicyContext(BaseModel):
    environment: Optional[str] = None
    stage: Optional[str] = None
    risk_level: Optional[str] = None
    readiness_state: Optional[str] = None
    incident_state: Optional[str] = None
    release_state: Optional[str] = None
    time_window: Optional[Dict[str, datetime]] = None
    ownership: Optional[str] = None

    model_config = {"frozen": True}


class PolicyRef(BaseModel):
    policy_id: str
    version: str = "1.0.0"


class PolicyRule(BaseModel):
    rule_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    rule_class: RuleClass
    subject_classes: List[SubjectClass]
    action_classes: List[ActionClass]
    resource_classes: List[ResourceClass]
    description: str


class PolicyInvariant(BaseModel):
    invariant_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    invariant_class: InvariantClass
    description: str
    proof_notes: str


class PolicyObligation(BaseModel):
    obligation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    obligation_class: ObligationClass
    description: str
    lineage_refs: List[str] = Field(default_factory=list)


class PolicyDefinition(BaseModel):
    policy_id: str
    policy_class: PolicyClass
    rules: List[PolicyRule] = Field(default_factory=list)
    invariants: List[PolicyInvariant] = Field(default_factory=list)
    obligations: List[PolicyObligation] = Field(default_factory=list)
    effective_from: datetime = Field(default_factory=utcnow)
    effective_until: Optional[datetime] = None
    description: str


class PolicyVerdict(BaseModel):
    verdict_class: VerdictClass
    reason: str
    proof_notes: str


class PolicyEvaluationRecord(BaseModel):
    evaluation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    subject: PolicySubject
    action: PolicyAction
    resource: PolicyResource
    context: PolicyContext
    verdict: PolicyVerdict
    evaluated_policies: List[str]
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyConflictRecord(BaseModel):
    conflict_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    involved_rule_ids: List[str]
    description: str
    severity: ConflictSeverity
    resolved: bool = False
    resolution_notes: Optional[str] = None
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyPrecedenceRecord(BaseModel):
    precedence_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    winning_rule_id: str
    losing_rule_ids: List[str]
    reason: str
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyExceptionRecord(BaseModel):
    exception_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    exception_class: ExceptionClass
    policy_id: str
    scope_constraints: Dict[str, Any]
    ttl_minutes: int
    reason: str
    issuer_id: str
    issued_at: datetime = Field(default_factory=utcnow)
    expires_at: datetime


class PolicyWaiverRecord(BaseModel):
    waiver_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    policy_id: str
    requester_id: str
    approver_id: Optional[str] = None
    reason: str
    scope_constraints: Dict[str, Any]
    issued_at: datetime = Field(default_factory=utcnow)
    expires_at: datetime
    revoked: bool = False


class PolicyDebtRecord(BaseModel):
    debt_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source_type: str  # 'waiver', 'exception', 'conflict', 'dead_rule'
    source_id: str
    severity: str
    description: str
    created_at: datetime = Field(default_factory=utcnow)
    resolved: bool = False


class PolicyEquivalenceReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    action: PolicyAction
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    divergence_notes: Optional[str] = None
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyDivergenceReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source_environment: str
    target_environment: str
    divergence_reason: str
    severity: str
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyTrustVerdict(BaseModel):
    trust_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    verdict: TrustVerdict
    factors: Dict[str, str]
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyAuditRecord(BaseModel):
    audit_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str
    details: str
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyArtifactManifest(BaseModel):
    manifest_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    policy_refs: List[PolicyRef]
    evaluation_ids: List[str]
    conflict_ids: List[str]
    exception_ids: List[str]
    debt_ids: List[str]
    hashes: Dict[str, str]
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyPlaneConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
