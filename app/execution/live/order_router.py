import logging
from typing import Any
from datetime import datetime
from decimal import Decimal
from app.execution.live.base import OrderRouterBase, OrderStateStoreBase
from app.execution.live.models import (
    ExecutionRequest,
    ExecutionResult,
    CancelRequest,
    CancelResult,
    ReplaceRequest,
    ExecutionConfig,
    OrderStateSnapshot,
    SubmittedOrder,
)
from app.execution.live.enums import OrderLifecycleStatus
from app.execution.live.pretrade_validation import PretradeValidator
from app.execution.live.safety_gates import SafetyGateManager
from app.execution.live.client_order_ids import ClientOrderIdGenerator

logger = logging.getLogger(__name__)


class OrderRouter(OrderRouterBase):
    def __init__(
        self,
        config: ExecutionConfig,
        executor: Any,
        state_store: OrderStateStoreBase,
        validator: PretradeValidator,
        gates: SafetyGateManager,
        id_generator: ClientOrderIdGenerator,
    ):
        self.config = config
        self.executor = executor
        self.state_store = state_store
        self.validator = validator
        self.gates = gates
        self.id_generator = id_generator

    async def submit_intent(self, intent: Any) -> ExecutionResult:
        # 1. Safety Gates
        gate_result = self.gates.evaluate_all(self.config, {"intent": intent})
        if not gate_result.passed:
            logger.error(f"Safety gate blocked intent: {gate_result.reason}")
            return ExecutionResult(
                success=False,
                client_order_id="",
                status=OrderLifecycleStatus.REJECTED,
                message=gate_result.reason,
            )

        # 2. Validation
        try:
            self.validator.validate(intent)
        except Exception as e:
            logger.error(f"Pretrade validation failed: {e}")
            return ExecutionResult(
                success=False,
                client_order_id="",
                status=OrderLifecycleStatus.REJECTED,
                message=str(e),
            )

        # 3. ID Generation
        client_order_id = self.id_generator.generate(
            intent.symbol, intent.side.value, intent.intent_id
        )

        # 4. Create Request
        request = ExecutionRequest(
            intent=intent,
            client_order_id=client_order_id,
            environment=self.config.environment,
        )

        return await self.submit_order(request)

    async def submit_order(self, request: ExecutionRequest) -> ExecutionResult:
        # Local state creation
        initial_state = OrderStateSnapshot(
            client_order_id=request.client_order_id,
            symbol=request.intent.symbol,
            status=OrderLifecycleStatus.PENDING_SUBMIT,
            last_update=datetime.utcnow(),
            is_open=True,
        )
        self.state_store.save_state(initial_state)

        try:
            ack = await self.executor.submit_order(request)

            # Update state to ACKNOWLEDGED
            initial_state.status = OrderLifecycleStatus.ACKNOWLEDGED
            initial_state.exchange_order_id = ack.exchange_order_id
            initial_state.last_update = datetime.utcnow()
            self.state_store.save_state(initial_state)

            return ExecutionResult(
                success=True,
                client_order_id=request.client_order_id,
                status=OrderLifecycleStatus.ACKNOWLEDGED,
            )
        except Exception as e:
            initial_state.status = OrderLifecycleStatus.REJECTED
            initial_state.is_open = False
            initial_state.last_update = datetime.utcnow()
            self.state_store.save_state(initial_state)
            return ExecutionResult(
                success=False,
                client_order_id=request.client_order_id,
                status=OrderLifecycleStatus.REJECTED,
                message=str(e),
            )

    async def cancel_order(self, request: CancelRequest) -> CancelResult:
        # Delegation to cancel_replace engine normally, or simple pass-through if Engine uses Router
        pass

    async def replace_order(self, request: ReplaceRequest) -> ExecutionResult:
        pass
