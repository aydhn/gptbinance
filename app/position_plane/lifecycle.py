from decimal import Decimal
from typing import Optional
from datetime import datetime, timezone
import uuid

from app.position_plane.enums import LifecycleState, Side
from app.position_plane.models import PositionState, PositionLifecycleEvent
from app.position_plane.exceptions import InvalidLifecycleTransitionError


class LifecycleManager:
    VALID_TRANSITIONS = {
        LifecycleState.FLAT: [LifecycleState.OPENING, LifecycleState.HEDGED_OPEN],
        LifecycleState.OPENING: [
            LifecycleState.OPEN,
            LifecycleState.CLOSED,
            LifecycleState.REVERSING,
        ],
        LifecycleState.OPEN: [
            LifecycleState.SCALING_IN,
            LifecycleState.SCALING_OUT,
            LifecycleState.CLOSED,
            LifecycleState.REVERSING,
            LifecycleState.HEDGED_OPEN,
        ],
        LifecycleState.SCALING_IN: [LifecycleState.OPEN],
        LifecycleState.SCALING_OUT: [
            LifecycleState.OPEN,
            LifecycleState.CLOSED,
            LifecycleState.DUST_RESIDUAL,
        ],
        LifecycleState.REVERSING: [LifecycleState.OPENING, LifecycleState.FLAT],
        LifecycleState.CLOSED: [LifecycleState.OPENING, LifecycleState.FLAT],
        LifecycleState.DUST_RESIDUAL: [
            LifecycleState.CLOSED,
            LifecycleState.FLAT,
            LifecycleState.OPENING,
        ],
        LifecycleState.HEDGED_OPEN: [
            LifecycleState.OPEN,
            LifecycleState.CLOSED,
            LifecycleState.FLAT,
        ],
    }

    @staticmethod
    def transition(
        state: PositionState,
        new_state: LifecycleState,
        reason: str,
        source_ref_id: Optional[str] = None,
    ) -> PositionLifecycleEvent:
        if new_state not in LifecycleManager.VALID_TRANSITIONS.get(
            state.lifecycle_state, []
        ):
            # Allow self transitions for SCALING
            if (
                state.lifecycle_state
                in [LifecycleState.SCALING_IN, LifecycleState.SCALING_OUT]
                and state.lifecycle_state == new_state
            ):
                pass
            else:
                raise InvalidLifecycleTransitionError(
                    f"Invalid transition from {state.lifecycle_state.value} to {new_state.value}"
                )

        event = PositionLifecycleEvent(
            event_id=str(uuid.uuid4()),
            state_id=state.id,
            previous_lifecycle=state.lifecycle_state,
            new_lifecycle=new_state,
            reason=reason,
            timestamp=datetime.now(timezone.utc),
            source_ref_id=source_ref_id,
        )

        state.lifecycle_state = new_state
        state.updated_at = datetime.now(timezone.utc)
        return event

    @staticmethod
    def determine_next_state(
        current_state: LifecycleState,
        current_qty: Decimal,
        delta_qty: Decimal,
        side: Side,
        fill_side: Side,
    ) -> LifecycleState:
        if current_qty == Decimal("0"):
            return LifecycleState.OPENING

        if side == fill_side:
            return LifecycleState.SCALING_IN

        if abs(delta_qty) < current_qty:
            return LifecycleState.SCALING_OUT

        if abs(delta_qty) == current_qty:
            return LifecycleState.CLOSED

        if abs(delta_qty) > current_qty:
            return LifecycleState.REVERSING

        return current_state
