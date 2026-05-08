import pytest
from app.execution_plane.venues import create_default_venue_registry
from app.execution_plane.enums import ProductClass

def test_venue_registry_creation():
    registry = create_default_venue_registry()
    assert len(registry.list_venues()) == 3

    spot_venues = registry.get_venues_by_product(ProductClass.SPOT)
    assert len(spot_venues) == 2

    futures_venues = registry.get_venues_by_product(ProductClass.USDT_MARGINED_FUTURES)
    assert len(futures_venues) == 1
    assert futures_venues[0].constraints.reduce_only_allowed is True
