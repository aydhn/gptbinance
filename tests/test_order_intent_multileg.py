from datetime import datetime, timezone
from app.order_intent.models import HighLevelIntent, IntentContext, AccountModeSnapshot
from app.order_intent.enums import IntentType, VenueProduct, OrderSide
from app.order_intent.multileg import IntentCompiler


def test_spot_single_leg():
    intent = HighLevelIntent(
        intent_id="test_int",
        intent_type=IntentType.OPEN_LONG,
        symbol="BTCUSDT",
        product=VenueProduct.SPOT,
        side=OrderSide.BUY,
        size=1.0,
        workspace_id="ws",
        profile_id="pr",
        created_at=datetime.now(timezone.utc),
    )
    ctx = IntentContext(
        account_snapshot=AccountModeSnapshot(
            timestamp=datetime.now(timezone.utc), active_modes=[]
        )
    )
    compiler = IntentCompiler()
    plan = compiler.compile_intent(intent, ctx)

    assert len(plan.legs) == 1
    assert plan.plan_type.value == "single_leg"


def test_margin_borrow_backed():
    intent = HighLevelIntent(
        intent_id="test_int",
        intent_type=IntentType.MARGIN_BORROW_BACKED_BUY,
        symbol="BTCUSDT",
        product=VenueProduct.MARGIN_CROSS,
        side=OrderSide.BUY,
        size=2.0,
        workspace_id="ws",
        profile_id="pr",
        created_at=datetime.now(timezone.utc),
    )
    ctx = IntentContext(
        account_snapshot=AccountModeSnapshot(
            timestamp=datetime.now(timezone.utc), active_modes=[]
        ),
        available_balance=1.0,
    )
    compiler = IntentCompiler()
    plan = compiler.compile_intent(intent, ctx)

    assert len(plan.legs) == 2
    assert plan.plan_type.value == "multi_leg"
    assert plan.legs[0].leg_type.value == "margin_borrow"
    assert plan.legs[1].leg_type.value == "margin_trade"
    assert plan.legs[0].leg_id in plan.legs[1].dependency_leg_ids
