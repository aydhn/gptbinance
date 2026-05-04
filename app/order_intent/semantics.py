from typing import Optional
from app.order_intent.enums import VenueProduct, PositionMode, OrderSide, PositionSide
from app.order_intent.models import VenueSemanticsProfile
from app.order_intent.exceptions import VenueSemanticsError


class SemanticsResolver:
    PROFILES = {
        VenueProduct.SPOT: VenueSemanticsProfile(
            product=VenueProduct.SPOT,
            requires_position_side=False,
            supports_reduce_only=False,
            supports_close_position=False,
            supports_borrow=False,
        ),
        VenueProduct.MARGIN_CROSS: VenueSemanticsProfile(
            product=VenueProduct.MARGIN_CROSS,
            requires_position_side=False,
            supports_reduce_only=False,  # Margin doesn't use standard futures reduceOnly, it repays.
            supports_close_position=False,
            supports_borrow=True,
        ),
        VenueProduct.MARGIN_ISOLATED: VenueSemanticsProfile(
            product=VenueProduct.MARGIN_ISOLATED,
            requires_position_side=False,
            supports_reduce_only=False,
            supports_close_position=False,
            supports_borrow=True,
        ),
        VenueProduct.FUTURES_USDM: VenueSemanticsProfile(
            product=VenueProduct.FUTURES_USDM,
            requires_position_side=True,  # Conditionally true based on hedge mode, handled in check
            supports_reduce_only=True,
            supports_close_position=True,
            supports_borrow=False,
        ),
        VenueProduct.FUTURES_COINM: VenueSemanticsProfile(
            product=VenueProduct.FUTURES_COINM,
            requires_position_side=True,
            supports_reduce_only=True,
            supports_close_position=True,
            supports_borrow=False,
        ),
    }

    @classmethod
    def get_profile(cls, product: VenueProduct) -> VenueSemanticsProfile:
        if product not in cls.PROFILES:
            raise VenueSemanticsError(f"No semantics profile for product: {product}")
        return cls.PROFILES[product]

    @classmethod
    def resolve_position_side(
        cls,
        product: VenueProduct,
        position_mode: Optional[PositionMode],
        side: OrderSide,
        intended_position_side: Optional[PositionSide] = None,
    ) -> Optional[PositionSide]:
        profile = cls.get_profile(product)

        if not profile.requires_position_side and intended_position_side is not None:
            raise VenueSemanticsError(
                f"Product {product} does not support position_side"
            )

        if product in [VenueProduct.FUTURES_USDM, VenueProduct.FUTURES_COINM]:
            if position_mode == PositionMode.HEDGE:
                if intended_position_side is None:
                    raise VenueSemanticsError(
                        "Hedge mode requires explicit position_side (LONG or SHORT)"
                    )
                if intended_position_side == PositionSide.BOTH:
                    raise VenueSemanticsError(
                        "Hedge mode cannot use BOTH position_side"
                    )
                return intended_position_side
            elif position_mode == PositionMode.ONE_WAY:
                if (
                    intended_position_side is not None
                    and intended_position_side != PositionSide.BOTH
                ):
                    raise VenueSemanticsError(
                        "One-way mode must use BOTH position_side or None (implicit BOTH)"
                    )
                return PositionSide.BOTH
        return None
