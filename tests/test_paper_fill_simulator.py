import pytest
from app.execution.paper.models import PaperOrder, PaperOrderStatus, FillTrigger
from app.execution.paper.fill_simulator import PaperFillSimulator
from datetime import datetime


def test_fill_simulator_next_tick():
    sim = PaperFillSimulator(FillTrigger.NEXT_TICK, 0.0, 0.0, 0.0)
    order = PaperOrder(
        order_id="o1",
        intent_id="i1",
        symbol="BTC",
        side="BUY",
        qty=1.0,
        status=PaperOrderStatus.ACCEPTED,
        created_at=datetime.utcnow(),
    )

    fills = sim.evaluate([order], current_price=50000.0, is_closed_bar=False)
    assert len(fills) == 1
    assert fills[0].price == 50000.0


def test_fill_simulator_slippage():
    sim = PaperFillSimulator(FillTrigger.NEXT_TICK, 0.01, 0.0, 0.0)
    order = PaperOrder(
        order_id="o1",
        intent_id="i1",
        symbol="BTC",
        side="BUY",
        qty=1.0,
        status=PaperOrderStatus.ACCEPTED,
        created_at=datetime.utcnow(),
    )

    fills = sim.evaluate([order], current_price=100.0, is_closed_bar=False)
    assert len(fills) == 1
    assert fills[0].price == 101.0  # +1% slippage for BUY

    order2 = PaperOrder(
        order_id="o2",
        intent_id="i2",
        symbol="BTC",
        side="SELL",
        qty=1.0,
        status=PaperOrderStatus.ACCEPTED,
        created_at=datetime.utcnow(),
    )
    fills2 = sim.evaluate([order2], current_price=100.0, is_closed_bar=False)
    assert len(fills2) == 1
    assert fills2[0].price == 99.0  # -1% slippage for SELL
