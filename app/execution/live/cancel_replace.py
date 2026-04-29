from typing import Any
import logging
from app.execution.live.models import (
    CancelRequest,
    CancelResult,
    ReplaceRequest,
    ExecutionResult,
)
from app.execution.live.base import OrderStateStoreBase
from app.execution.live.enums import OrderLifecycleStatus

logger = logging.getLogger(__name__)


class CancelReplaceEngine:
    def __init__(self, state_store: OrderStateStoreBase, executor: Any, router: Any):
        self.state_store = state_store
        self.executor = executor
        self.router = router

    async def execute_cancel(self, request: CancelRequest) -> CancelResult:
        state = self.state_store.get_state(request.client_order_id)
        if not state:
            logger.warning(
                f"Attempted to cancel unknown order {request.client_order_id}"
            )
            return CancelResult(
                success=False,
                client_order_id=request.client_order_id,
                status=OrderLifecycleStatus.UNKNOWN,
                message="Order not found",
            )

        if not state.is_open:
            logger.warning(
                f"Attempted to cancel closed order {request.client_order_id} (status: {state.status})"
            )
            return CancelResult(
                success=False,
                client_order_id=request.client_order_id,
                status=state.status,
                message="Order already closed",
            )

        try:
            response = await self.executor.cancel_order(request)
            # We assume user stream or REST response updates the state store.
            # For immediate reflection, we can optimistically set pending.
            state.status = OrderLifecycleStatus.PENDING_CANCEL
            self.state_store.save_state(state)

            return CancelResult(
                success=True,
                client_order_id=request.client_order_id,
                status=OrderLifecycleStatus.CANCELED,  # Ideally verified from response
                message="Cancel requested",
            )
        except Exception as e:
            return CancelResult(
                success=False,
                client_order_id=request.client_order_id,
                status=state.status,
                message=str(e),
            )

    async def execute_replace(self, request: ReplaceRequest) -> ExecutionResult:
        # 1. Cancel original
        cancel_req = CancelRequest(
            client_order_id=request.original_client_order_id,
            symbol=request.new_intent.symbol,
            reason="Replace",
        )
        cancel_result = await self.execute_cancel(cancel_req)

        if not cancel_result.success:
            logger.error(
                f"Failed to cancel original order {request.original_client_order_id} for replacement."
            )
            return ExecutionResult(
                success=False,
                client_order_id=request.original_client_order_id,
                status=cancel_result.status,
                message=cancel_result.message,
            )

        # 2. Submit new (using router to go through validation & ids)
        # Assuming router handles intent -> request conversion
        logger.info(f"Successfully cancelled original order, submitting replacement.")
        # Note: In a real system, we must ensure the cancel actually completed on the exchange
        # before submitting the new order to avoid double exposure.
        return await self.router.submit_intent(request.new_intent)
