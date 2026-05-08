from decimal import Decimal
from typing import Dict, Any, List

from app.position_plane.models import PositionState
from app.position_plane.lots import LotManager
from app.position_plane.realized import RealizedPnLCalculator


class ReductionManager:
    @staticmethod
    def apply_reduction(state: PositionState, fill: Dict[str, Any]) -> List[Any]:
        fill_qty = Decimal(str(fill["quantity"]))
        close_price = Decimal(str(fill["price"]))
        fill_id = fill.get("fill_id", "unknown")

        remaining_to_consume = fill_qty
        realized_records = []

        for lot in state.open_lots:
            if not lot.is_closed:
                consumed_amount = min(remaining_to_consume, lot.remaining_quantity)
                lot, remaining = LotManager.consume_lot(lot, consumed_amount)

                realized_record = RealizedPnLCalculator.calculate_from_reduction(
                    lot, consumed_amount, close_price, fill_id
                )
                realized_records.append(realized_record)

                remaining_to_consume -= consumed_amount
                if remaining_to_consume == Decimal("0"):
                    break

        return realized_records
