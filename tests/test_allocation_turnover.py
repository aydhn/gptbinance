from app.allocation.turnover import TurnoverEngine
from app.allocation.models import AllocationCandidate
from app.allocation.enums import SignalFamily, AllocationClass


def test_turnover():
    engine = TurnoverEngine()
    cand = AllocationCandidate(
        candidate_id="c1",
        symbol="BTC",
        signal_source_ref="s1",
        signal_family=SignalFamily.MOMENTUM,
        sleeve_ref="primary_alpha_01",
        confidence=1.0,
        requested_notional=50.0,
        allocation_class=AllocationClass.DIRECTIONAL_LONG,
    )
    findings = engine.evaluate([cand])
    assert findings[0].is_churn == True
