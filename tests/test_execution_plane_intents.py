from app.execution_plane.intents import ExecutionPlanBuilder
from app.execution_plane.models import ExecutionCandidate, OrderSpec, RoutingPolicy
from app.execution_plane.enums import RoutingClass, OrderType, TIFClass


def test_plan_builder():
    c = ExecutionCandidate(
        allocation_intent_id="a1",
        symbol="x",
        target_size=1,
        side="buy",
        is_reduce_only=False,
        venue_eligibility=[],
        instrument_compatibility=True,
        size_viable=True,
    )
    o = OrderSpec(
        candidate_id="c",
        venue_id="v",
        symbol="x",
        side="buy",
        order_type=OrderType.MARKET,
        tif=TIFClass.IOC,
        qty=1,
        client_order_id="1",
    )
    r = RoutingPolicy(
        routing_class=RoutingClass.PASSIVE,
        urgency="low",
        rationale="",
        max_slippage_bps=1,
    )

    plan = ExecutionPlanBuilder.build("a1", c, o, r, ["guard_ok"])
    assert plan.source_allocation_intent_id == "a1"
    assert len(plan.entries) == 1
    assert "v" in plan.venue_scope
