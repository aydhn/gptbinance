from datetime import datetime
from app.risk.exposure import ExposureCalculator
from app.backtest.models import PositionState
from app.backtest.enums import PositionSide


def test_exposure_calculation():
    calc = ExposureCalculator()
    p1 = PositionState(
        symbol="BTC", side=PositionSide.LONG, quantity=1.0, entry_price=50000.0
    )
    p2 = PositionState(
        symbol="ETH", side=PositionSide.SHORT, quantity=10.0, entry_price=3000.0
    )

    snap = calc.calculate([p1, p2], equity=100000.0, timestamp=datetime.now())

    assert snap.total_long_exposure == 50000.0
    assert snap.total_short_exposure == 30000.0
    assert snap.total_gross_exposure == 80000.0
    assert snap.symbol_exposures["BTC"] == 50000.0
    assert snap.symbol_exposures["ETH"] == 30000.0
