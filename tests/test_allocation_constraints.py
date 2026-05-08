from app.allocation.constraints import ConstraintRegistry, ConstraintEvaluator
from app.allocation.models import AllocationCandidate, PortfolioExposureSnapshot
from app.allocation.enums import SignalFamily, AllocationClass
from datetime import datetime, timezone


def test_constraints():
    registry = ConstraintRegistry()
    evaluator = ConstraintEvaluator(registry)

    cand = AllocationCandidate(
        candidate_id="c1",
        symbol="BTC",
        signal_source_ref="s1",
        signal_family=SignalFamily.MOMENTUM,
        sleeve_ref="primary_alpha_01",
        confidence=1.0,
        requested_notional=300000.0,
        allocation_class=AllocationClass.DIRECTIONAL_LONG,
    )
    snap = PortfolioExposureSnapshot(
        snapshot_id="1",
        timestamp=datetime.now(timezone.utc),
        gross_notional=0.0,
        net_notional=0.0,
        sleeve_exposures={},
        symbol_exposures={},
    )

    reasons = evaluator.evaluate(cand, snap)
    assert "constraint_violation_global_max_gross" in reasons
