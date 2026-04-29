import pytest
from decimal import Decimal
import uuid
from app.execution.live.order_router import OrderRouter
from app.execution.live.models import ExecutionConfig, ExecutionIntent
from app.execution.live.enums import ExecutionEnvironment, OrderLifecycleStatus
from app.execution.live.pretrade_validation import PretradeValidator
from app.execution.live.safety_gates import SafetyGateManager
from app.execution.live.client_order_ids import ClientOrderIdGenerator
from app.execution.live.order_state_store import InMemoryOrderStateStore
from app.core.models import OrderSide, OrderType


class MockExecutor:
    async def submit_order(self, req):
        from app.execution.live.models import ExchangeAck

        return ExchangeAck(
            client_order_id=req.client_order_id,
            exchange_order_id="ex123",
            raw_response={},
        )


class MockGates(SafetyGateManager):
    def evaluate_all(self, config, context):
        from app.execution.live.models import SafeExecutionGateResult

        return SafeExecutionGateResult(passed=True)


@pytest.mark.asyncio
async def test_order_router_submit():
    config = ExecutionConfig()
    executor = MockExecutor()
    store = InMemoryOrderStateStore()
    validator = PretradeValidator({"BTCUSDT": {}})
    gates = MockGates()  # Empty, so it passes
    id_gen = ClientOrderIdGenerator("SESS")

    router = OrderRouter(config, executor, store, validator, gates, id_gen)
    intent = ExecutionIntent(
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=Decimal("1"),
        intent_id="i1",
    )

    res = await router.submit_intent(intent)
    assert res.success
    assert res.status == OrderLifecycleStatus.ACKNOWLEDGED

    state = store.get_state(res.client_order_id)
    assert state.exchange_order_id == "ex123"
