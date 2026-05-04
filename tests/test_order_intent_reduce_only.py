import pytest
from app.order_intent.models import CompiledOrderLeg, IntentContext, AccountModeSnapshot
from app.order_intent.enums import VenueProduct, OrderLegType, OrderSide
from app.order_intent.reduce_only import ReduceOnlyCompiler
from app.order_intent.exceptions import ReduceOnlyViolation
from datetime import datetime, timezone


def test_reduce_only_valid():
    leg = CompiledOrderLeg(
        leg_id="test",
        leg_type=OrderLegType.FUTURES_TRADE,
        symbol="BTCUSDT",
        product=VenueProduct.FUTURES_USDM,
        side=OrderSide.SELL,
        size=1.0,
        reduce_only=True,
    )
    ctx = IntentContext(
        account_snapshot=AccountModeSnapshot(
            timestamp=datetime.now(timezone.utc), active_modes=[]
        ),
        existing_exposure=2.0,
    )
    compiler = ReduceOnlyCompiler()
    res = compiler.apply(leg, ctx)
    assert res.reduce_only is True


def test_reduce_only_invalid_side():
    leg = CompiledOrderLeg(
        leg_id="test",
        leg_type=OrderLegType.FUTURES_TRADE,
        symbol="BTCUSDT",
        product=VenueProduct.FUTURES_USDM,
        side=OrderSide.BUY,
        size=1.0,
        reduce_only=True,
    )
    ctx = IntentContext(
        account_snapshot=AccountModeSnapshot(
            timestamp=datetime.now(timezone.utc), active_modes=[]
        ),
        existing_exposure=2.0,
    )
    compiler = ReduceOnlyCompiler()
    with pytest.raises(ReduceOnlyViolation):
        compiler.apply(leg, ctx)
