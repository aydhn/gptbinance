from pydantic.v1 import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from app.control_plane.enums import (
    CommandClass,
    ActionClass,
    PreviewClass,
    ExceptionClass,
    RollbackClass,
    ScopeClass,
    TrustVerdict,
    KillSwitchClass,
    EquivalenceVerdict,
)


class ControlPlaneConfig(BaseModel):
    is_enabled: bool = True


class CommandDefinition(BaseModel):
    command_id: CommandClass
    action_class: ActionClass
    required_scope: ScopeClass
    requires_preview: bool
    requires_approval: bool
    reversibility: RollbackClass


class CommandRef(BaseModel):
    command_id: CommandClass
    version: str = "1.0"


class ActionRequest(BaseModel):
    action_id: str
    command_id: CommandClass
    actor: str
    scope_class: ScopeClass
    scope_ref: str
    intent: str
    payload: Dict[str, Any]
    requested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionPreview(BaseModel):
    action_id: str
    preview_class: PreviewClass
    affected_entities: List[str]
    blocked_downstream_actions: List[str]
    blast_radius_summary: str
    reversibility_summary: str
    staleness_caveats: List[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionDryRunResult(BaseModel):
    action_id: str
    fidelity_class: PreviewClass
    hypothetical_receipts: List[str]
    simulated_outcomes: Dict[str, Any]
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionApprovalChain(BaseModel):
    action_id: str
    required_approvals: int = 1
    current_approvals: int = 0
    approvers: List[str] = Field(default_factory=list)


class ApprovalDecision(BaseModel):
    action_id: str
    approver: str
    is_approved: bool
    rationale: str
    conditions: List[str] = Field(default_factory=list)
    decided_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionApplyRecord(BaseModel):
    receipt_id: str
    action_id: str
    outcome: str
    applied_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionRollbackRecord(BaseModel):
    action_id: str
    rollback_receipt_id: str
    actor: str
    outcome: str
    rolled_back_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionRevokeRecord(BaseModel):
    target_id: str  # approval_id or token_id or pause_id
    actor: str
    reason: str
    revoked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ExceptionToken(BaseModel):
    token_id: str
    action_id: str
    exception_class: ExceptionClass
    scope_ref: str
    ttl_seconds: int
    rationale: str
    is_revoked: bool = False
    issued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class KillSwitchRecord(BaseModel):
    kill_switch_id: str
    kill_switch_class: KillSwitchClass
    actor: str
    scope_ref: str
    is_active: bool = True
    issued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FreezeRecord(BaseModel):
    freeze_id: str
    scope_class: ScopeClass
    scope_ref: str
    actor: str
    is_active: bool = True
    issued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class UnfreezeRecord(BaseModel):
    freeze_id: str
    actor: str
    reason: str
    unfrozen_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ScopePauseRecord(BaseModel):
    pause_id: str
    scope_class: ScopeClass
    scope_ref: str
    actor: str
    is_active: bool = True
    issued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ControlReceipt(BaseModel):
    receipt_id: str
    action_id: str
    actor: str
    approvers: List[str]
    preview_hash: str
    dry_run_hash: Optional[str] = None
    apply_outcome: str
    affected_artefacts: List[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ControlEquivalenceReport(BaseModel):
    action_id: str
    verdict: EquivalenceVerdict
    divergence_reasons: List[str]
    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ControlDivergenceReport(BaseModel):
    action_id: str
    divergence_type: str
    severity: str
    details: str
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ControlTrustVerdict(BaseModel):
    verdict: TrustVerdict
    reasons: List[str]
    action_history_summary: Dict[str, int]
    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ControlAuditRecord(BaseModel):
    action_id: str
    events: List[str]


class ControlArtifactManifest(BaseModel):
    manifest_id: str
    action_id: str
    receipt_id: str
    hashes: Dict[str, str]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
