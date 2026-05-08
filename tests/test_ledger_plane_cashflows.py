import pytest
from app.ledger_plane.cashflows import CashflowBuilder
from app.ledger_plane.enums import CashflowClass


def test_cashflow_creation():
    cashflow = CashflowBuilder.build(
        cashflow_class=CashflowClass.TRADE,
        asset="BTC",
        amount=1.5,
        account_scope="binance_spot",
        direction="in",
    )
    assert cashflow.cashflow_class == CashflowClass.TRADE
    assert cashflow.asset == "BTC"
    assert cashflow.amount == 1.5
    assert cashflow.direction == "in"
    assert cashflow.id is not None
