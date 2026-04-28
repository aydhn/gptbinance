from datetime import datetime
from app.backtest.position_state import PositionManager
from app.backtest.models import SimulatedFill, SimulatedOrderIntent, FillModelDecision
from app.backtest.enums import PositionSide, OrderSide


def test_position_long_entry():
    pm = PositionManager("BTCUSDT")
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        quantity=1.0,
        intent_source="test",
    )
    decision = FillModelDecision(
        accepted=True,
        fill_price=100.0,
        fill_quantity=1.0,
        fill_timestamp=datetime.now(),
        fee_paid=0.1,
        slippage_applied=0.0,
    )
    fill = SimulatedFill(
        fill_id="1", timestamp=datetime.now(), intent=intent, decision=decision
    )

    state, pnl = pm.apply_fill(fill)
    assert state.side == PositionSide.LONG
    assert state.quantity == 1.0
    assert state.entry_price == 100.0
    assert pnl == 0.0


def test_position_short_entry():
    pm = PositionManager("BTCUSDT")
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        side=OrderSide.SELL,
        quantity=1.0,
        intent_source="test",
    )
    decision = FillModelDecision(
        accepted=True,
        fill_price=100.0,
        fill_quantity=1.0,
        fill_timestamp=datetime.now(),
    )
    fill = SimulatedFill(
        fill_id="1", timestamp=datetime.now(), intent=intent, decision=decision
    )

    state, pnl = pm.apply_fill(fill)
    assert state.side == PositionSide.SHORT
    assert state.quantity == 1.0
    assert state.entry_price == 100.0
