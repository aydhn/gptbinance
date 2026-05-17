import pytest
from app.state_plane.models import StateObject, LifecycleDefinition
from app.state_plane.registry import state_registry
from app.state_plane.desired import set_desired_state
from app.state_plane.effective import set_effective_state
from app.state_plane.reconciliation import reconcile_state
from app.state_plane.transitions import record_transition
from app.state_plane.exceptions import IllegalStateJumpError

def test_integration_flow():
    # Setup Lifecycle
    lc = LifecycleDefinition(
        lifecycle_id="release_lifecycle",
        states=["planned", "ready", "canary", "live", "terminal"],
        terminal_states=["terminal"]
    )
    state_registry.register_lifecycle(lc)

    # Register Object
    obj = StateObject(state_id="rel_1", object_class="release", lifecycle_id="release_lifecycle")
    state_registry.register_object(obj)

    # Target state
    set_desired_state("rel_1", "live")

    # Try illegal transition
    with pytest.raises(IllegalStateJumpError):
        record_transition("rel_1", "planned", "unknown_state")

    # Legal transitions
    record_transition("rel_1", "planned", "ready")
    record_transition("rel_1", "ready", "canary")

    # Effective state is canary, but desired is live -> not converged
    set_effective_state("rel_1", "canary")
    rec = reconcile_state("rel_1")
    assert rec.is_converged is False

    # Now complete to live
    record_transition("rel_1", "canary", "live")
    set_effective_state("rel_1", "live")
    rec = reconcile_state("rel_1")
    assert rec.is_converged is True
