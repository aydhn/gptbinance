from typing import Dict, Optional, List
from app.execution_plane.models import VenueDefinition, VenueConstraint
from app.execution_plane.enums import VenueClass, ProductClass
from app.execution_plane.exceptions import InvalidVenueDefinitionError


class VenueRegistry:
    def __init__(self):
        self._venues: Dict[str, VenueDefinition] = {}

    def register_venue(self, venue: VenueDefinition):
        if not venue.is_active:
            raise InvalidVenueDefinitionError(
                f"Cannot register inactive venue: {venue.venue_id}"
            )
        self._venues[venue.venue_id] = venue

    def get_venue(self, venue_id: str) -> Optional[VenueDefinition]:
        return self._venues.get(venue_id)

    def list_venues(self) -> List[VenueDefinition]:
        return list(self._venues.values())

    def get_venues_by_product(
        self, product_class: ProductClass
    ) -> List[VenueDefinition]:
        return [v for v in self._venues.values() if v.product_class == product_class]


# Canonical Venue Factory
def create_default_venue_registry() -> VenueRegistry:
    registry = VenueRegistry()

    # Binance Spot Mainnet
    binance_spot = VenueDefinition(
        venue_id="binance_spot_mainnet",
        venue_class=VenueClass.BINANCE_SPOT_MAINNET,
        product_class=ProductClass.SPOT,
        constraints=VenueConstraint(
            min_notional=5.0,  # e.g. 5 USDT
            min_qty=0.00001,
            step_size=0.00001,
            tick_size=0.01,
            price_band_pct=5.0,
            reduce_only_allowed=False,  # Not applicable for spot
            margin_modes_allowed=["cross", "isolated"],
            is_fresh=True,
            evidence_ref="static_default",
        ),
        metadata={"maker_fee": 0.001, "taker_fee": 0.001},
    )
    registry.register_venue(binance_spot)

    # Binance Futures Mainnet
    binance_futures = VenueDefinition(
        venue_id="binance_futures_mainnet",
        venue_class=VenueClass.BINANCE_FUTURES_MAINNET,
        product_class=ProductClass.USDT_MARGINED_FUTURES,
        constraints=VenueConstraint(
            min_notional=5.0,
            min_qty=0.001,
            step_size=0.001,
            tick_size=0.01,
            price_band_pct=5.0,
            reduce_only_allowed=True,
            margin_modes_allowed=["cross", "isolated"],
            is_fresh=True,
            evidence_ref="static_default",
        ),
        metadata={"maker_fee": 0.0002, "taker_fee": 0.0004},
    )
    registry.register_venue(binance_futures)

    # Paper
    paper_spot = VenueDefinition(
        venue_id="paper_spot",
        venue_class=VenueClass.PAPER,
        product_class=ProductClass.SPOT,
        constraints=VenueConstraint(
            min_notional=0.0,
            min_qty=0.00001,
            step_size=0.00001,
            tick_size=0.01,
            price_band_pct=100.0,
            reduce_only_allowed=True,
            margin_modes_allowed=["cross", "isolated"],
            is_fresh=True,
            evidence_ref="paper_env",
        ),
        metadata={"maker_fee": 0.0, "taker_fee": 0.0},
    )
    registry.register_venue(paper_spot)

    return registry
