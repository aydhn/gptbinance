import pytest
from app.backtest.derivatives.positions import BacktestDerivativePositionState

def test_short_pnl():
    state = BacktestDerivativePositionState()
    # Open short
    pnl1 = state.apply_fill("BTC", False, 1.0, 100.0)
    assert pnl1 == 0.0
    assert state.positions["BTC"] == -1.0

    # Close short at lower price (profit)
    pnl2 = state.apply_fill("BTC", True, 1.0, 80.0)
    assert pnl2 == 20.0
    assert state.positions["BTC"] == 0.0
