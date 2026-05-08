from app.execution_plane.routing import RoutingEngine
from app.execution_plane.models import ExecutionCandidate
from app.execution_plane.enums import RoutingClass


def test_routing_engine():
    cand1 = ExecutionCandidate(
        allocation_intent_id="a1",
        symbol="BTCUSDT",
        target_size=1.0,
        side="buy",
        is_reduce_only=False,
        venue_eligibility=["v1"],
        instrument_compatibility=True,
        size_viable=True,
    )
    policy1 = RoutingEngine.evaluate(cand1, max_slippage_bps=10.0)
    assert policy1.routing_class == RoutingClass.PASSIVE

    cand2 = ExecutionCandidate(
        allocation_intent_id="a2",
        symbol="BTCUSDT",
        target_size=50.0,
        side="buy",
        is_reduce_only=False,
        venue_eligibility=["v1"],
        instrument_compatibility=True,
        size_viable=True,
    )
    policy2 = RoutingEngine.evaluate(cand2, max_slippage_bps=10.0)
    assert policy2.routing_class == RoutingClass.STAGED_SLICE
