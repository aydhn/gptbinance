from .models import DerivativeExecutionIntent, ReduceOnlyExecutionRequest
from .enums import ReduceOnlyVerdict, DerivativeSide
from typing import Tuple

class ReduceOnlyValidator:
    @staticmethod
    def validate(request: ReduceOnlyExecutionRequest) -> Tuple[ReduceOnlyVerdict, float, str]:
        """
        Validates if an order is strictly reduce-only.
        Returns: Verdict, adjusted quantity (if ADJUSTED), rationale
        """
        intent = request.intent
        current_qty = request.current_position_qty

        if not intent.is_reduce_only:
            return ReduceOnlyVerdict.ALLOWED, intent.quantity, "Not a reduce-only order."

        if current_qty == 0:
            return ReduceOnlyVerdict.REJECTED, 0.0, "Cannot reduce position: current position is 0."

        is_current_long = current_qty > 0

        if is_current_long and intent.side == DerivativeSide.LONG:
            return ReduceOnlyVerdict.REJECTED, 0.0, "Reduce-only long intent rejected: current position is long (would increase position)."

        if not is_current_long and intent.side == DerivativeSide.SHORT:
             return ReduceOnlyVerdict.REJECTED, 0.0, "Reduce-only short intent rejected: current position is short (would increase position)."

        abs_current_qty = abs(current_qty)
        if intent.quantity > abs_current_qty:
            return ReduceOnlyVerdict.ADJUSTED, abs_current_qty, f"Reduce-only intent adjusted: {intent.quantity} -> {abs_current_qty} to prevent flipping position."

        return ReduceOnlyVerdict.ALLOWED, intent.quantity, "Reduce-only order valid."
