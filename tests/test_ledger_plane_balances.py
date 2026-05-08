import pytest
from app.ledger_plane.balances import BalanceStateBuilder
from app.ledger_plane.buckets import BalanceBucketBuilder
from app.ledger_plane.enums import BalanceClass

def test_balance_state_creation():
    bucket = BalanceBucketBuilder.build(
        bucket_class=BalanceClass.AVAILABLE,
        amount=1000.0,
        asset="USDT"
    )
    state = BalanceStateBuilder.build(
        account_scope="binance_futures",
        asset="USDT",
        buckets=[bucket],
        authoritative=True
    )
    assert state.account_scope == "binance_futures"
    assert state.asset == "USDT"
    assert len(state.buckets) == 1
    assert state.buckets[0].amount == 1000.0
    assert state.authoritative is True
