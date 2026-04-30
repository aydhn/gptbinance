import pytest
from app.execution.derivatives.carry_costs import CarryCostAccounting
from app.products.enums import ProductType

def test_carry_cost_accumulation():
    costs = CarryCostAccounting()
    costs.add_funding_charge("BTCUSDT", 10.0)
    costs.add_funding_charge("BTCUSDT", -2.0)

    snap = costs.get_carry_cost_snapshot(ProductType.FUTURES_USDM, "BTCUSDT")
    assert snap.total_accrued_cost == 8.0
    assert snap.funding_snapshot is not None
