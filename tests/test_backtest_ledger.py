from datetime import datetime
from app.backtest.ledger import Ledger
from app.backtest.models import SimulatedFill, SimulatedOrderIntent, FillModelDecision
from app.backtest.enums import PositionSide, OrderSide


def test_ledger_trade_lifecycle():
    ledger = Ledger()

    intent1 = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=OrderSide.BUY,
        quantity=1.0,
        intent_source="test",
    )
    decision1 = FillModelDecision(
        accepted=True,
        fill_price=100.0,
        fill_quantity=1.0,
        fill_timestamp=datetime.now(),
    )
    fill1 = SimulatedFill(
        fill_id="1", timestamp=datetime.now(), intent=intent1, decision=decision1
    )

    ledger.record_fill(fill1, PositionSide.FLAT, PositionSide.LONG)
    assert len(ledger.trades) == 1
    assert ledger.trades[0].status.name == "OPEN"

    intent2 = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=OrderSide.SELL,
        quantity=1.0,
        intent_source="test",
    )
    decision2 = FillModelDecision(
        accepted=True,
        fill_price=110.0,
        fill_quantity=1.0,
        fill_timestamp=datetime.now(),
    )
    fill2 = SimulatedFill(
        fill_id="2", timestamp=datetime.now(), intent=intent2, decision=decision2
    )
    fill2.realized_pnl = 10.0

    ledger.record_fill(fill2, PositionSide.LONG, PositionSide.FLAT)
    assert len(ledger.trades) == 1
    assert ledger.trades[0].status.name == "CLOSED"
    assert ledger.trades[0].realized_pnl == 10.0
