from app.allocation.capacity import CapacityEngine
from app.allocation.models import AllocationCandidate
from app.allocation.enums import SignalFamily, AllocationClass


def test_capacity():
    engine = CapacityEngine()
    cand = AllocationCandidate(
        candidate_id="c1",
        symbol="BTC",
        signal_source_ref="s1",
        signal_family=SignalFamily.MOMENTUM,
        sleeve_ref="primary_alpha_01",
        confidence=1.0,
        requested_notional=60000.0,
        allocation_class=AllocationClass.DIRECTIONAL_LONG,
    )
    findings = engine.evaluate([cand])
    assert len(findings) == 1
    assert findings[0].is_capacity_breach == True
