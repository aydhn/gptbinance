import pytest
from app.ledger_plane.buckets import BalanceBucketBuilder
from app.ledger_plane.enums import BalanceClass

def test_balance_bucket_creation():
    bucket = BalanceBucketBuilder.build(
        bucket_class=BalanceClass.LOCKED,
        amount=50.0,
        asset="BNB"
    )
    assert bucket.bucket_class == BalanceClass.LOCKED
    assert bucket.amount == 50.0
    assert bucket.asset == "BNB"
