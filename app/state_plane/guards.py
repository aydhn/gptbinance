from typing import Callable, Dict, List
from .models import StateObject
from .registry import state_registry
from .exceptions import GuardViolationError

class TransitionGuard:
    def __init__(self, name: str, check_fn: Callable[[StateObject], bool], error_msg: str):
        self.name = name
        self.check_fn = check_fn
        self.error_msg = error_msg

_guards: Dict[str, List[TransitionGuard]] = {}

def register_guard(transition_key: str, guard: TransitionGuard):
    if transition_key not in _guards:
        _guards[transition_key] = []
    _guards[transition_key].append(guard)

def evaluate_guards(state_id: str, from_state: str, to_state: str):
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    key = f"{obj.lifecycle_id}:{from_state}->{to_state}"
    for guard in _guards.get(key, []):
        if not guard.check_fn(obj):
            raise GuardViolationError(f"Guard '{guard.name}' failed: {guard.error_msg}")
