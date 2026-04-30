import pytest
from app.execution.derivatives.reduce_only import ReduceOnlyValidator, ReduceOnlyExecutionRequest
from app.execution.derivatives.models import DerivativeExecutionIntent
from app.execution.derivatives.enums import DerivativeSide, ReduceOnlyVerdict
from app.products.enums import ProductType

def test_reduce_only_rejection_when_increasing():
    intent = DerivativeExecutionIntent(
        product_type=ProductType.FUTURES_USDM, symbol="BTCUSDT", side=DerivativeSide.LONG, quantity=1.0, is_reduce_only=True
    )
    req = ReduceOnlyExecutionRequest(intent=intent, current_position_qty=2.0) # Already long
    verdict, _, _ = ReduceOnlyValidator.validate(req)
    assert verdict == ReduceOnlyVerdict.REJECTED

def test_reduce_only_adjustment():
    intent = DerivativeExecutionIntent(
        product_type=ProductType.FUTURES_USDM, symbol="BTCUSDT", side=DerivativeSide.SHORT, quantity=5.0, is_reduce_only=True
    )
    req = ReduceOnlyExecutionRequest(intent=intent, current_position_qty=2.0) # Long 2.0, trying to short 5.0
    verdict, adj_qty, _ = ReduceOnlyValidator.validate(req)
    assert verdict == ReduceOnlyVerdict.ADJUSTED
    assert adj_qty == 2.0
