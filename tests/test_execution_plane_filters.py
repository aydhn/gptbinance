import pytest
from app.execution_plane.venues import create_default_venue_registry
from app.execution_plane.filters import VenueFilterEngine
from app.execution_plane.models import OrderSpec
from app.execution_plane.enums import OrderType, TIFClass
from app.execution_plane.exceptions import VenueConstraintViolationError

def test_venue_filter_engine():
    registry = create_default_venue_registry()
    venue = registry.get_venue("binance_spot_mainnet")

    spec = OrderSpec(
        candidate_id="c1", venue_id=venue.venue_id, symbol="BTCUSDT",
        side="buy", order_type=OrderType.LIMIT, tif=TIFClass.GTC,
        qty=0.000001, # Too small
        price=50000.0, client_order_id="x"
    )

    with pytest.raises(VenueConstraintViolationError):
        VenueFilterEngine.validate(spec, venue)

    spec.qty = 1.0 # OK qty
    assert VenueFilterEngine.validate(spec, venue) is True

    spec.is_reduce_only = True
    with pytest.raises(VenueConstraintViolationError):
        # Spot shouldn't allow reduce_only
        VenueFilterEngine.validate(spec, venue)
