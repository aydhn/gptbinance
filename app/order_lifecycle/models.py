from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.order_lifecycle.enums import (
    LifecycleState,
    AttemptStatus,
    TransitionType,
    CancelVerdict,
    ReplaceVerdict,
    TimeoutClass,
    OrphanSeverity,
    DedupVerdict,
    LifecycleVerdict,
    EventSource,
)


class OrderLifecycleConfig(BaseModel):
    pass


class ExecutionPlanRef(BaseModel):
    plan_id: str
    leg_id: str


class OrderLineageRef(BaseModel):
    client_order_id: str
    parent_attempt_id: Optional[str] = None
    compiled_leg_id: str


class IdempotencyKey(BaseModel):
    key: str
    context: Dict[str, Any] = Field(default_factory=dict)


class OrderAttemptRef(BaseModel):
    attempt_id: str
    client_order_id: str


class LifecycleTransition(BaseModel):
    transition_id: str
    attempt_id: str
    from_state: LifecycleState
    to_state: LifecycleState
    transition_type: TransitionType
    timestamp: datetime
    explanation: str = ""
    metadata: Dict[str, Any] = Field(default_factory=dict)


class OrderLifecycleState(BaseModel):
    current_state: LifecycleState
    last_updated: datetime
    terminal: bool = False
    unresolved: bool = False


class OrderAttempt(BaseModel):
    attempt_id: str
    lineage: OrderLineageRef
    idempotency_key: IdempotencyKey
    state: OrderLifecycleState
    created_at: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SubmitRequest(BaseModel):
    attempt_id: str
    payload: Dict[str, Any]


class SubmitResult(BaseModel):
    attempt_id: str
    success: bool
    error: Optional[str] = None


class VenueAck(BaseModel):
    attempt_id: str
    venue_order_id: str
    timestamp: datetime


class VenueReject(BaseModel):
    attempt_id: str
    reason: str
    timestamp: datetime


class PartialFill(BaseModel):
    attempt_id: str
    fill_id: str
    price: float
    quantity: float
    timestamp: datetime


class FullFill(BaseModel):
    attempt_id: str
    fill_id: str
    price: float
    quantity: float
    timestamp: datetime


class CancelRequest(BaseModel):
    attempt_id: str
    reason: str


class CancelResult(BaseModel):
    attempt_id: str
    success: bool
    verdict: CancelVerdict


class ReplaceRequest(BaseModel):
    old_attempt_id: str
    new_attempt_id: str
    price: Optional[float] = None
    quantity: Optional[float] = None


class ReplaceResult(BaseModel):
    success: bool
    verdict: ReplaceVerdict


class TimeoutResolution(BaseModel):
    attempt_id: str
    timeout_class: TimeoutClass
    resolved_state: LifecycleState
    timestamp: datetime


class OrphanOrderRecord(BaseModel):
    orphan_id: str
    venue_order_id: str
    severity: OrphanSeverity
    timestamp: datetime
    remediation_notes: str = ""


class DeadLetterEvent(BaseModel):
    event_id: str
    payload: Dict[str, Any]
    source: EventSource
    timestamp: datetime


class LifecycleAuditRecord(BaseModel):
    run_id: str
    attempt_id: str
    verdict: LifecycleVerdict
    timestamp: datetime


class LifecycleArtifactManifest(BaseModel):
    run_id: str
    attempt_ids: List[str]
    timestamp: datetime
