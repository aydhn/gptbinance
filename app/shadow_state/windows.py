from app.shadow_state.models import EventualConsistencyWindow
from app.shadow_state.enums import ConsistencyWindow


def get_consistency_windows() -> dict[ConsistencyWindow, EventualConsistencyWindow]:
    """Returns the default tolerances for eventual consistency."""
    return {
        ConsistencyWindow.SUBMIT_ACK_TOLERANCE: EventualConsistencyWindow(
            window_type=ConsistencyWindow.SUBMIT_ACK_TOLERANCE,
            grace_period_ms=5000,
            is_active=True,
        ),
        ConsistencyWindow.FILL_PROPAGATION: EventualConsistencyWindow(
            window_type=ConsistencyWindow.FILL_PROPAGATION,
            grace_period_ms=10000,
            is_active=True,
        ),
        ConsistencyWindow.CANCEL_PERSISTENCE: EventualConsistencyWindow(
            window_type=ConsistencyWindow.CANCEL_PERSISTENCE,
            grace_period_ms=8000,
            is_active=True,
        ),
        ConsistencyWindow.TIMEOUT_UNKNOWN_CAUTION: EventualConsistencyWindow(
            window_type=ConsistencyWindow.TIMEOUT_UNKNOWN_CAUTION,
            grace_period_ms=30000,
            is_active=True,
        ),
        ConsistencyWindow.LIVE_CAUTION_STRICT: EventualConsistencyWindow(
            window_type=ConsistencyWindow.LIVE_CAUTION_STRICT,
            grace_period_ms=2000,
            is_active=True,
        ),
    }
