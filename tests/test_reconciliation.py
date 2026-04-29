import pytest
from app.execution.live.reconciliation import ReconciliationEngine
from app.execution.live.order_state_store import InMemoryOrderStateStore
from app.execution.live.models import OrderStateSnapshot
from app.execution.live.enums import OrderLifecycleStatus, ReconciliationStatus
from datetime import datetime


class MockBinanceClient:
    pass


class TestReconciliationEngine(ReconciliationEngine):
    async def fetch_exchange_open_orders(self):
        return [{"clientOrderId": "c2"}]


@pytest.mark.asyncio
async def test_reconciliation_drift():
    store = InMemoryOrderStateStore()
    store.save_state(
        OrderStateSnapshot(
            client_order_id="c1",
            symbol="BTC",
            status=OrderLifecycleStatus.ACKNOWLEDGED,
            is_open=True,
            last_update=datetime.utcnow(),
        )
    )

    engine = TestReconciliationEngine(store, MockBinanceClient())
    report = await engine.run_reconciliation()

    assert report.status == ReconciliationStatus.DRIFT_DETECTED
    assert len(report.drift_items) == 1
    assert "c1" in report.drift_items[0]
