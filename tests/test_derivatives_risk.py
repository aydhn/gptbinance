import pytest
from app.risk.derivatives import DerivativeRiskController
from app.products.registry import ProductRegistry
from app.products.enums import ProductType

def test_risk_cap():
    reg = ProductRegistry()
    risk = DerivativeRiskController(reg)
    assert not risk.check_leverage_cap(ProductType.FUTURES_USDM, 100)
