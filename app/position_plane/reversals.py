from decimal import Decimal
from typing import Dict, Any, List

from app.position_plane.models import PositionState
from app.position_plane.reductions import ReductionManager
from app.position_plane.lots import LotManager


class ReversalManager:
    @staticmethod
    def apply_reversal(state: PositionState, fill: Dict[str, Any]) -> List[Any]:
        # Close the existing position completely
        close_qty = state.quantity
        close_fill = fill.copy()
        close_fill["quantity"] = str(close_qty)

        realized_records = ReductionManager.apply_reduction(state, close_fill)

        # Determine remaining quantity for the new side
        total_fill_qty = Decimal(str(fill["quantity"]))
        new_side_qty = total_fill_qty - close_qty

        if new_side_qty > Decimal("0"):
            open_fill = fill.copy()
            open_fill["quantity"] = str(new_side_qty)
            new_lot = LotManager.create_lot_from_fill(open_fill, state.sleeve_id)
            state.open_lots.append(new_lot)
            state.quantity = new_side_qty
            state.side = open_fill["side"]
        else:
            state.quantity = Decimal("0")

        return realized_records
