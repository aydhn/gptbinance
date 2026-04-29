import pytest
from app.execution.live.cancel_replace import CancelReplaceEngine
from app.execution.live.models import CancelRequest, OrderStateSnapshot
from app.execution.live.enums import OrderLifecycleStatus
from app.execution.live.order_state_store import InMemoryOrderStateStore
from datetime import datetime


class MockExecutor:
    async def cancel_order(self, req):
        return {"status": "CANCELED"}


@pytest.mark.asyncio
async def test_execute_cancel_unknown_order():
    store = InMemoryOrderStateStore()
    engine = CancelReplaceEngine(store, MockExecutor(), None)
    req = CancelRequest(client_order_id="unknown", symbol="BTCUSDT", reason="test")
    res = await engine.execute_cancel(req)
    assert not res.success
    assert res.message == "Order not found"


@pytest.mark.asyncio
async def test_execute_cancel_success():
    store = InMemoryOrderStateStore()
    store.save_state(
        OrderStateSnapshot(
            client_order_id="c1",
            symbol="BTCUSDT",
            status=OrderLifecycleStatus.ACKNOWLEDGED,
            is_open=True,
            last_update=datetime.utcnow(),
        )
    )

    engine = CancelReplaceEngine(store, MockExecutor(), None)
    req = CancelRequest(client_order_id="c1", symbol="BTCUSDT", reason="test")
    res = await engine.execute_cancel(req)

    assert res.success
    state = store.get_state("c1")
    assert state.status == OrderLifecycleStatus.PENDING_CANCEL
