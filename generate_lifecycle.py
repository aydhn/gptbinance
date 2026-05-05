import os

files = {
    "app/order_lifecycle/enums.py": """from enum import Enum

class LifecycleState(str, Enum):
    CREATED = "CREATED"
    READY_TO_SUBMIT = "READY_TO_SUBMIT"
    SUBMITTED_PENDING_ACK = "SUBMITTED_PENDING_ACK"
    ACKNOWLEDGED_OPEN = "ACKNOWLEDGED_OPEN"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FULLY_FILLED = "FULLY_FILLED"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCELLED = "CANCELLED"
    REPLACE_REQUESTED = "REPLACE_REQUESTED"
    REPLACED = "REPLACED"
    REJECTED = "REJECTED"
    TIMEOUT_UNKNOWN = "TIMEOUT_UNKNOWN"
    ORPHANED = "ORPHANED"
    DEAD_LETTERED = "DEAD_LETTERED"

class AttemptStatus(str, Enum):
    ACTIVE = "ACTIVE"
    TERMINAL = "TERMINAL"
    AMBIGUOUS = "AMBIGUOUS"

class TransitionType(str, Enum):
    INITIALIZE = "INITIALIZE"
    SUBMIT = "SUBMIT"
    ACK = "ACK"
    REJECT = "REJECT"
    PARTIAL_FILL = "PARTIAL_FILL"
    FULL_FILL = "FULL_FILL"
    REQUEST_CANCEL = "REQUEST_CANCEL"
    CANCEL_ACK = "CANCEL_ACK"
    CANCEL_REJECT = "CANCEL_REJECT"
    REQUEST_REPLACE = "REQUEST_REPLACE"
    REPLACE_ACK = "REPLACE_ACK"
    REPLACE_REJECT = "REPLACE_REJECT"
    MARK_TIMEOUT = "MARK_TIMEOUT"
    MARK_ORPHAN = "MARK_ORPHAN"
    MARK_DEAD_LETTER = "MARK_DEAD_LETTER"

class CancelVerdict(str, Enum):
    ALLOWED = "ALLOWED"
    FORBIDDEN_TERMINAL = "FORBIDDEN_TERMINAL"
    FORBIDDEN_RACE = "FORBIDDEN_RACE"

class ReplaceVerdict(str, Enum):
    ALLOWED = "ALLOWED"
    FORBIDDEN_REDUCE_ONLY_BREAK = "FORBIDDEN_REDUCE_ONLY_BREAK"
    FORBIDDEN_TERMINAL = "FORBIDDEN_TERMINAL"

class TimeoutClass(str, Enum):
    PENDING_ACK_TIMEOUT = "PENDING_ACK_TIMEOUT"
    CANCEL_TIMEOUT = "CANCEL_TIMEOUT"
    STALE_PARTIAL_FILL = "STALE_PARTIAL_FILL"

class OrphanSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class DedupVerdict(str, Enum):
    NEW_EVENT = "NEW_EVENT"
    DUPLICATE_EVENT = "DUPLICATE_EVENT"
    CONFLICTING_EVENT = "CONFLICTING_EVENT"

class LifecycleVerdict(str, Enum):
    HEALTHY = "HEALTHY"
    CAUTION = "CAUTION"
    UNRESOLVED = "UNRESOLVED"

class EventSource(str, Enum):
    VENUE_WS = "VENUE_WS"
    VENUE_REST = "VENUE_REST"
    INTERNAL_TIMEOUT = "INTERNAL_TIMEOUT"
    MANUAL_RECONCILE = "MANUAL_RECONCILE"
""",
    "app/order_lifecycle/exceptions.py": """class OrderLifecycleError(Exception):
    pass

class InvalidLifecycleTransitionError(OrderLifecycleError):
    pass

class DuplicateSubmitError(OrderLifecycleError):
    pass

class IdempotencyViolationError(OrderLifecycleError):
    pass

class VenueEventMappingError(OrderLifecycleError):
    pass

class OrphanOrderError(OrderLifecycleError):
    pass

class TimeoutResolutionError(OrderLifecycleError):
    pass

class ReplaceConflictError(OrderLifecycleError):
    pass

class CancelConflictError(OrderLifecycleError):
    pass

class LifecycleStorageError(OrderLifecycleError):
    pass
""",
    "app/order_lifecycle/models.py": """from pydantic import BaseModel, Field
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
""",
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
