import pytest
from app.ledger_plane.equity import EquityViewBuilder
from app.ledger_plane.enums import EquityClass

def test_equity_view_creation():
    equity = EquityViewBuilder.build(
        account_scope="binance_futures",
        equity_class=EquityClass.PNL_ADJUSTED,
        total_value=1500.0,
        currency="USDT"
    )
    assert equity.account_scope == "binance_futures"
    assert equity.equity_class == EquityClass.PNL_ADJUSTED
    assert equity.total_value == 1500.0
    assert equity.currency == "USDT"
