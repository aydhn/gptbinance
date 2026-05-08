from decimal import Decimal
from typing import List
from app.position_plane.models import PositionState


class HedgeEvaluator:
    @staticmethod
    def evaluate_hedge_truth(
        long_states: List[PositionState], short_states: List[PositionState]
    ) -> Decimal:
        long_qty = sum(state.quantity for state in long_states)
        short_qty = sum(state.quantity for state in short_states)
        return min(long_qty, short_qty)
