from app.execution.live.order_state_store import InMemoryOrderStateStore
from app.execution.live.models import OrderStateSnapshot
from app.execution.live.enums import OrderLifecycleStatus
from datetime import datetime
from decimal import Decimal


def test_order_state_store():
    store = InMemoryOrderStateStore()
    snapshot = OrderStateSnapshot(
        client_order_id="c1",
        symbol="BTCUSDT",
        status=OrderLifecycleStatus.PENDING_SUBMIT,
        last_update=datetime.utcnow(),
        is_open=True,
    )
    store.save_state(snapshot)

    retrieved = store.get_state("c1")
    assert retrieved is not None
    assert retrieved.client_order_id == "c1"

    open_orders = store.get_all_open_orders()
    assert len(open_orders) == 1

    snapshot.is_open = False
    store.save_state(snapshot)

    open_orders2 = store.get_all_open_orders()
    assert len(open_orders2) == 0
