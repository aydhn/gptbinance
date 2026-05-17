from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
import uuid

def now_utc():
    return datetime.now(timezone.utc)

@dataclass
class StateObjectRef:
    object_id: str
    object_class: str

@dataclass
class StatePlaneConfig:
    enabled: bool = True

@dataclass
class LifecycleDefinition:
    lifecycle_id: str
    states: List[str]
    terminal_states: List[str]

@dataclass
class DesiredStateRecord:
    state_id: str
    desired_state: str
    authority: str = "operator"
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class DeclaredStateRecord:
    state_id: str
    declared_state: str
    authority: str = "control-plane"
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class ObservedStateRecord:
    state_id: str
    observed_state: str
    authority: str = "telemetry"
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class EffectiveStateRecord:
    state_id: str
    effective_state: str
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class ReconciledStateRecord:
    state_id: str
    reconciled_state: str
    is_converged: bool
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class TransitionRecord:
    state_id: str
    from_state: str
    to_state: str
    transition_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class SplitBrainRecord:
    state_id: str
    observed_state: str
    declared_state: str
    severity: str
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class StateObject:
    state_id: str
    object_class: str
    lifecycle_id: str
    desired: Optional[DesiredStateRecord] = None
    declared: Optional[DeclaredStateRecord] = None
    observed: Optional[ObservedStateRecord] = None
    effective: Optional[EffectiveStateRecord] = None
    reconciled: Optional[ReconciledStateRecord] = None
    split_brain: Optional[SplitBrainRecord] = None
    transitions: List[TransitionRecord] = field(default_factory=list)

@dataclass
class StateTrustVerdict:
    state_id: str
    verdict: str # trusted, caution, degraded, blocked, review_required
    reasons: List[str]
    timestamp: datetime = field(default_factory=now_utc)

@dataclass
class StateEquivalenceReport:
    state_id: str
    is_equivalent: bool
    divergences: List[str]
    timestamp: datetime = field(default_factory=now_utc)
