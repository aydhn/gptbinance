import pytest
from app.execution.paper.derivatives_runtime import PaperDerivativesRuntime
from app.execution.derivatives.pretrade_validation import DerivativePretradeValidator
from app.execution.derivatives.leverage import LeverageManager
from app.products.registry import ProductRegistry
from app.products.enums import ProductType
from app.execution.derivatives.models import DerivativeExecutionIntent
from app.execution.derivatives.enums import DerivativeSide


def test_paper_derivatives_runtime():
    reg = ProductRegistry()
    lev = LeverageManager(reg)
    validator = DerivativePretradeValidator(reg, lev)
    runtime = PaperDerivativesRuntime(validator, lev)

    intent = DerivativeExecutionIntent(
        product_type=ProductType.FUTURES_USDM,
        symbol="BTCUSDT",
        side=DerivativeSide.LONG,
        quantity=1.0,
    )

    # Should process successfully
    assert runtime.process_intent(intent, 0.0, 50000.0, 1000.0)
