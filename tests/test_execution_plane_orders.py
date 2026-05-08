import pytest
from app.execution_plane.orders import OrderSpecValidator
from app.execution_plane.models import OrderSpec
from app.execution_plane.enums import OrderType, TIFClass
from app.execution_plane.exceptions import InvalidOrderSpecError

def test_order_spec_validator():
    spec = OrderSpec(
        candidate_id="c1", venue_id="v1", symbol="BTCUSDT",
        side="buy", order_type=OrderType.LIMIT, tif=TIFClass.GTC,
        qty=1.0, client_order_id="x"
    )
    # limit without price
    with pytest.raises(InvalidOrderSpecError):
        OrderSpecValidator.validate(spec)

    spec.price = 50000.0
    assert OrderSpecValidator.validate(spec) is True

    spec.order_type = OrderType.MARKET
    spec.is_post_only = True
    # market + post_only
    with pytest.raises(InvalidOrderSpecError):
        OrderSpecValidator.validate(spec)
