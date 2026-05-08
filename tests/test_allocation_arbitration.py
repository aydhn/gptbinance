from app.allocation.arbitration import ArbitrationEngine
from app.allocation.sleeves import SleeveRegistry
from app.allocation.models import AllocationCandidate
from app.allocation.enums import SignalFamily, AllocationClass


def test_arbitration():
    registry = SleeveRegistry()
    engine = ArbitrationEngine(registry)

    cand1 = AllocationCandidate(
        candidate_id="c1",
        symbol="BTC",
        signal_source_ref="s1",
        signal_family=SignalFamily.MOMENTUM,
        sleeve_ref="primary_alpha_01",
        confidence=0.5,
        requested_notional=100.0,
        allocation_class=AllocationClass.DIRECTIONAL_LONG,
    )
    cand2 = AllocationCandidate(
        candidate_id="c2",
        symbol="ETH",
        signal_source_ref="s2",
        signal_family=SignalFamily.MOMENTUM,
        sleeve_ref="hedge_overlay_01",
        confidence=0.8,
        requested_notional=100.0,
        allocation_class=AllocationClass.DIRECTIONAL_LONG,
    )

    sorted_cands = engine.arbitrate([cand1, cand2])
    # hedge overlay has conflict priority 200 vs primary_alpha 100
    assert sorted_cands[0].candidate_id == "c2"
    assert sorted_cands[1].candidate_id == "c1"
