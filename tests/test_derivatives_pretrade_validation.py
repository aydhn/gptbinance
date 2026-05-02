import pytest
from app.products.registry import ProductRegistry
from app.products.enums import ProductType
from app.execution.derivatives.leverage import LeverageManager
from app.execution.derivatives.pretrade_validation import DerivativePretradeValidator
from app.execution.derivatives.models import DerivativeExecutionIntent
from app.execution.derivatives.enums import DerivativeSide


def test_pretrade_validation_leverage_cap():
    reg = ProductRegistry()
    lev = LeverageManager(reg)
    validator = DerivativePretradeValidator(reg, lev)

    # Set leverage above cap (bypassing normal manager checks for testing validation)
    lev._state[ProductType.FUTURES_USDM.value] = {"BTCUSDT": 100}

    intent = DerivativeExecutionIntent(
        product_type=ProductType.FUTURES_USDM,
        symbol="BTCUSDT",
        side=DerivativeSide.LONG,
        quantity=1.0,
    )
    assert not validator.validate_intent(intent, 0.0)


def test_pretrade_validation_success():
    reg = ProductRegistry()
    lev = LeverageManager(reg)
    validator = DerivativePretradeValidator(reg, lev)

    lev.set_leverage(ProductType.FUTURES_USDM, "BTCUSDT", 2)
    intent = DerivativeExecutionIntent(
        product_type=ProductType.FUTURES_USDM,
        symbol="BTCUSDT",
        side=DerivativeSide.LONG,
        quantity=1.0,
    )
    assert validator.validate_intent(intent, 0.0)
