from app.execution.live_runtime.base import FlattenControllerBase
from app.execution.live_runtime.models import LiveFlattenRequest, LiveFlattenResult
from app.execution.live_runtime.enums import FlattenMode
from typing import Any
import logging

logger = logging.getLogger(__name__)


class LiveFlattenController(FlattenControllerBase):
    def __init__(self, execution_gateway: Any, position_book: Any):
        self.execution_gateway = execution_gateway
        self.position_book = position_book

    def execute_flatten(self, request: LiveFlattenRequest) -> LiveFlattenResult:
        logger.warning(
            f"Flattening live session {request.run_id} via mode {request.mode.value} (Reason: {request.reason})"
        )

        cancelled = 0
        closed = 0
        errors = []

        try:
            # Cancel all open orders
            open_orders = getattr(
                self.execution_gateway, "get_open_orders", lambda: []
            )()
            for o in open_orders:
                try:
                    getattr(self.execution_gateway, "cancel_order", lambda *a: None)(
                        o.symbol, o.order_id
                    )
                    cancelled += 1
                except Exception as e:
                    errors.append(f"Failed to cancel {o.order_id}: {e}")

            # Close positions if requested
            if request.mode in [
                FlattenMode.CANCEL_AND_CLOSE,
                FlattenMode.EMERGENCY_MARKET,
            ]:
                pb = getattr(self.position_book, "get_book", lambda: None)()
                if pb:
                    for symbol, pos in pb.positions.items():
                        if pos.qty != 0:
                            side = "SELL" if pos.qty > 0 else "BUY"
                            try:
                                getattr(
                                    self.execution_gateway,
                                    "submit_market_order",
                                    lambda *a: None,
                                )(symbol=symbol, side=side, qty=abs(pos.qty))
                                closed += 1
                            except Exception as e:
                                errors.append(
                                    f"Failed to close position for {symbol}: {e}"
                                )

        except Exception as e:
            errors.append(f"Flatten execution error: {e}")

        success = len(errors) == 0

        return LiveFlattenResult(
            run_id=request.run_id,
            success=success,
            orders_cancelled=cancelled,
            positions_closed=closed,
            errors=errors,
        )
