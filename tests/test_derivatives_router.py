import pytest
from app.execution.derivatives.router import DerivativeRouter
from app.execution.derivatives.models import DerivativeExecutionIntent
from app.execution.derivatives.enums import DerivativeSide
from app.products.enums import ProductType

def test_router_routing():
    router = DerivativeRouter()
    intent = DerivativeExecutionIntent(product_type=ProductType.FUTURES_USDM, symbol="BTCUSDT", side=DerivativeSide.LONG, quantity=1.0)
    # The actual router just logs currently, ensure it doesn't throw
    router.route(intent, paper_mode=True)
    router.route(intent, paper_mode=False)
