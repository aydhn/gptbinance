import pytest
from app.order_intent.enums import VenueProduct, PositionMode, OrderSide, PositionSide
from app.order_intent.semantics import SemanticsResolver
from app.order_intent.exceptions import VenueSemanticsError


def test_spot_profile():
    profile = SemanticsResolver.get_profile(VenueProduct.SPOT)
    assert not profile.requires_position_side
    assert not profile.supports_reduce_only
    assert not profile.supports_close_position
    assert not profile.supports_borrow


def test_futures_profile():
    profile = SemanticsResolver.get_profile(VenueProduct.FUTURES_USDM)
    assert profile.requires_position_side
    assert profile.supports_reduce_only
    assert profile.supports_close_position
    assert not profile.supports_borrow


def test_resolve_position_side_hedge():
    side = SemanticsResolver.resolve_position_side(
        VenueProduct.FUTURES_USDM, PositionMode.HEDGE, OrderSide.BUY, PositionSide.LONG
    )
    assert side == PositionSide.LONG


def test_resolve_position_side_hedge_invalid():
    with pytest.raises(VenueSemanticsError):
        SemanticsResolver.resolve_position_side(
            VenueProduct.FUTURES_USDM, PositionMode.HEDGE, OrderSide.BUY, None
        )


def test_resolve_position_side_one_way():
    side = SemanticsResolver.resolve_position_side(
        VenueProduct.FUTURES_USDM, PositionMode.ONE_WAY, OrderSide.BUY, None
    )
    assert side == PositionSide.BOTH
