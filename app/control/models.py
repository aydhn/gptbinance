from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.control.enums import (
    SensitiveActionType,
    ActionCriticality,
    ApprovalStatus,
    AuthorizationVerdict,
    OperatorRole,
    RevocationReason,
    BreakGlassSeverity,
    CommandStatus,
    PolicySeverity,
)


class OperatorIdentity(BaseModel):
    id: str
    roles: List[OperatorRole]
    alias: Optional[str] = None


class ControlConfig(BaseModel):
    enabled: bool = True
    default_policy_severity: PolicySeverity = PolicySeverity.STRICT
    max_approval_ttl_seconds: int = 3600


class SensitiveAction(BaseModel):
    action_type: SensitiveActionType
    criticality: ActionCriticality
    required_roles: List[OperatorRole]
    min_approvals: int
    ttl_seconds: int
    allow_break_glass: bool
    description: str
    recommended_knowledge_refs: List[str] = Field(default_factory=list)


class ActionRequestContext(BaseModel):
    run_id: Optional[str] = None
    bundle_id: Optional[str] = None
    release_ref: Optional[str] = None
    session_ref: Optional[str] = None
    symbol_scope: Optional[List[str]] = None
    additional_metadata: Dict[str, Any] = Field(default_factory=dict)


class ActionRequest(BaseModel):
    id: str
    action_type: SensitiveActionType
    requester: OperatorIdentity
    context: ActionRequestContext
    rationale: str
    created_at: datetime
    expires_at: datetime


class ActionRequestSummary(BaseModel):
    id: str
    action_type: SensitiveActionType
    status: ApprovalStatus
    created_at: datetime


class ApprovalRequirement(BaseModel):
    min_approvals: int
    required_roles: List[OperatorRole]


class ApprovalDecision(BaseModel):
    request_id: str
    approver: OperatorIdentity
    approved: bool
    reason: Optional[str] = None
    timestamp: datetime


class ApprovalRecord(BaseModel):
    request: ActionRequest
    decisions: List[ApprovalDecision] = Field(default_factory=list)
    status: ApprovalStatus = ApprovalStatus.PENDING


class ApprovalQueueEntry(BaseModel):
    request_id: str
    action_type: SensitiveActionType
    status: ApprovalStatus
    expires_at: datetime


class AuthorizationResult(BaseModel):
    request_id: str
    verdict: AuthorizationVerdict
    reason: str
    readiness_advisory: Optional[str] = None
    timestamp: datetime
    is_break_glass: bool = False


class ApprovalPolicy(BaseModel):
    name: str
    severity: PolicySeverity


class ApprovalWindow(BaseModel):
    start_time: datetime
    end_time: datetime


class ApprovalExpiry(BaseModel):
    request_id: str
    expired_at: datetime
    reason: str
    readiness_advisory: Optional[str] = None


class RevocationRecord(BaseModel):
    request_id: str
    revoked_by: OperatorIdentity
    reason: RevocationReason
    timestamp: datetime


class BreakGlassRequest(BaseModel):
    request_id: str
    severity: BreakGlassSeverity
    justification: str


class BreakGlassDecision(BaseModel):
    request_id: str
    authorized_by: OperatorIdentity
    timestamp: datetime


class OperatorSessionRef(BaseModel):
    session_id: str
    operator_id: str


class CommandExecutionRef(BaseModel):
    command_id: str
    request_id: str


class CommandJournalEntry(BaseModel):
    id: str
    request_id: str
    action_type: SensitiveActionType
    requester_id: str
    status: CommandStatus
    timestamp: datetime
    details: Dict[str, Any] = Field(default_factory=dict)


class ControlAuditRecord(BaseModel):
    event_id: str
    event_type: str
    timestamp: datetime
    details: Dict[str, Any]


class ControlArtifactManifest(BaseModel):
    manifest_id: str
    entries: List[ControlAuditRecord] = Field(default_factory=list)
