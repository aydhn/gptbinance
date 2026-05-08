from decimal import Decimal
from typing import List

from app.position_plane.models import PositionLot
from app.position_plane.enums import CostBasisClass
from app.position_plane.exceptions import InvalidCostBasisStateError


class CostBasisCalculator:
    @staticmethod
    def calculate(
        lots: List[PositionLot],
        method: CostBasisClass = CostBasisClass.WEIGHTED_AVERAGE,
    ) -> Decimal:
        open_lots = [lot for lot in lots if not lot.is_closed]
        if not open_lots:
            return Decimal("0")

        if method == CostBasisClass.WEIGHTED_AVERAGE:
            total_notional = sum(
                lot.entry_price * lot.remaining_quantity for lot in open_lots
            )
            total_qty = sum(lot.remaining_quantity for lot in open_lots)
            if total_qty == Decimal("0"):
                return Decimal("0")
            return total_notional / total_qty

        elif method == CostBasisClass.FIFO_LOT:
            # Basic implementation; real implementation tracks specific lot consumption
            # Assuming lots are ordered by creation
            return open_lots[0].entry_price

        raise InvalidCostBasisStateError(
            f"Cost basis method {method} not implemented yet."
        )
