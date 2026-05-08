import pytest
from app.ledger_plane.collateral import CollateralTruthBuilder
from app.ledger_plane.enums import CollateralClass

def test_collateral_truth_creation():
    collateral = CollateralTruthBuilder.build(
        account_scope="binance_futures",
        asset="USDT",
        collateral_class=CollateralClass.USABLE,
        amount=500.0
    )
    assert collateral.account_scope == "binance_futures"
    assert collateral.asset == "USDT"
    assert collateral.collateral_class == CollateralClass.USABLE
    assert collateral.amount == 500.0
