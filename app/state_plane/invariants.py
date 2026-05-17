from typing import Callable, List
from .models import StateObject
from .registry import state_registry
from .exceptions import StatePlaneError

class InvariantViolationError(StatePlaneError):
    pass

class StateInvariant:
    def __init__(self, name: str, check_fn: Callable[[StateObject], bool]):
        self.name = name
        self.check_fn = check_fn

_invariants: List[StateInvariant] = []

def register_invariant(invariant: StateInvariant):
    _invariants.append(invariant)

def check_invariants(state_id: str):
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    violations = []
    for inv in _invariants:
        if not inv.check_fn(obj):
            violations.append(inv.name)

    if violations:
        raise InvariantViolationError(f"Invariants violated: {', '.join(violations)}")
