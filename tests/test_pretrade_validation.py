import pytest
from decimal import Decimal
from app.execution.live.pretrade_validation import PretradeValidator
from app.execution.live.models import ExecutionIntent
from app.execution.live.exceptions import PretradeValidationError
from app.core.models import OrderSide, OrderType


def test_pretrade_validation_passes():
    rules = {"BTCUSDT": {"minQty": Decimal("0.001"), "minNotional": Decimal("10")}}
    validator = PretradeValidator(rules)
    intent = ExecutionIntent(
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        quantity=Decimal("0.01"),
        price=Decimal("50000"),
        intent_id="1",
    )
    validator.validate(intent)  # Should not raise


def test_pretrade_validation_fails_min_qty():
    rules = {"BTCUSDT": {"minQty": Decimal("0.001")}}
    validator = PretradeValidator(rules)
    intent = ExecutionIntent(
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=Decimal("0.0001"),
        intent_id="1",
    )
    with pytest.raises(PretradeValidationError):
        validator.validate(intent)
