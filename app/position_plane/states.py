from typing import Dict, Any
from decimal import Decimal
import uuid

from app.position_plane.models import PositionState
from app.position_plane.enums import ProductClass, Side, LifecycleState
from app.position_plane.cost_basis import CostBasisCalculator
from app.position_plane.lifecycle import LifecycleManager
from app.position_plane.lots import LotManager


class PositionStateManager:
    @staticmethod
    def create_empty_state(
        symbol: str, product_class: ProductClass, sleeve_id: str
    ) -> PositionState:
        return PositionState(
            id=str(uuid.uuid4()),
            symbol=symbol,
            product_class=product_class,
            sleeve_id=sleeve_id,
            side=Side.FLAT,
            quantity=Decimal("0"),
            average_entry_price=Decimal("0"),
            lifecycle_state=LifecycleState.FLAT,
            is_authoritative=True,
        )

    @staticmethod
    def apply_fill(state: PositionState, fill: Dict[str, Any]) -> None:
        fill_qty = Decimal(str(fill["quantity"]))
        fill_side = Side(fill["side"])

        if state.quantity == Decimal("0") or state.side == Side.FLAT:
            new_lot = LotManager.create_lot_from_fill(fill, state.sleeve_id)
            state.open_lots.append(new_lot)
            state.quantity = fill_qty
            state.side = fill_side
            LifecycleManager.transition(state, LifecycleState.OPENING, "Initial fill")
            LifecycleManager.transition(state, LifecycleState.OPEN, "Settled")
        elif state.side == fill_side:
            # Increase position
            new_lot = LotManager.create_lot_from_fill(fill, state.sleeve_id)
            state.open_lots.append(new_lot)
            state.quantity += fill_qty
            LifecycleManager.transition(state, LifecycleState.SCALING_IN, "Scaling in")
            LifecycleManager.transition(state, LifecycleState.OPEN, "Settled")
        else:
            # Reduce or reverse position
            remaining_to_consume = fill_qty
            for lot in state.open_lots:
                if not lot.is_closed:
                    lot, remaining_to_consume = LotManager.consume_lot(
                        lot, remaining_to_consume
                    )
                    if remaining_to_consume == Decimal("0"):
                        break

            if remaining_to_consume > Decimal("0"):
                # Reversal
                state.open_lots = [lot for lot in state.open_lots if not lot.is_closed]
                state.quantity = remaining_to_consume
                state.side = fill_side

                # Create lot for the new side
                remaining_fill = fill.copy()
                remaining_fill["quantity"] = str(remaining_to_consume)
                new_lot = LotManager.create_lot_from_fill(
                    remaining_fill, state.sleeve_id
                )
                state.open_lots.append(new_lot)
                LifecycleManager.transition(
                    state, LifecycleState.REVERSING, "Reversing position"
                )
                LifecycleManager.transition(
                    state, LifecycleState.OPENING, "Reopening after reversal"
                )
                LifecycleManager.transition(
                    state, LifecycleState.OPEN, "Settled after reversal"
                )
            else:
                # Reduction
                state.quantity -= fill_qty
                if state.quantity <= Decimal("1e-8"):  # Dust threshold
                    state.quantity = Decimal("0")
                    state.side = Side.FLAT
                    LifecycleManager.transition(
                        state, LifecycleState.CLOSED, "Full close"
                    )
                else:
                    LifecycleManager.transition(
                        state, LifecycleState.SCALING_OUT, "Scaling out"
                    )
                    LifecycleManager.transition(state, LifecycleState.OPEN, "Settled")

        # Recalculate average entry price
        state.average_entry_price = CostBasisCalculator.calculate(state.open_lots)
        state.open_lots = [lot for lot in state.open_lots if not lot.is_closed]
