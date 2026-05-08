from app.allocation.diffs import DiffEngine
from app.allocation.models import AllocationManifest, AllocationIntent, TrustVerdict
from app.allocation.enums import AllocationVerdict
from datetime import datetime, timezone


def test_diffs():
    engine = DiffEngine()
    i1 = AllocationIntent(
        intent_id="i1",
        candidate_id="c1",
        symbol="BTC",
        sleeve_ref="s1",
        verdict=AllocationVerdict.ACCEPTED,
        base_size=10,
        clipped_size=10,
        budget_ref="b1",
        route_ref="r1",
    )
    i2 = AllocationIntent(
        intent_id="i1",
        candidate_id="c1",
        symbol="BTC",
        sleeve_ref="s1",
        verdict=AllocationVerdict.ACCEPTED,
        base_size=10,
        clipped_size=20,
        budget_ref="b1",
        route_ref="r1",
    )
    i3 = AllocationIntent(
        intent_id="i2",
        candidate_id="c2",
        symbol="ETH",
        sleeve_ref="s1",
        verdict=AllocationVerdict.ACCEPTED,
        base_size=10,
        clipped_size=10,
        budget_ref="b1",
        route_ref="r1",
    )

    m1 = AllocationManifest(
        manifest_id="m1",
        timestamp=datetime.now(timezone.utc),
        intents=[i1],
        portfolio_gross_exposure=10,
        portfolio_net_exposure=10,
        constraints_refs=[],
        trust_verdict=TrustVerdict.TRUSTED,
        lineage_hash="abc",
    )
    m2 = AllocationManifest(
        manifest_id="m2",
        timestamp=datetime.now(timezone.utc),
        intents=[i2, i3],
        portfolio_gross_exposure=30,
        portfolio_net_exposure=30,
        constraints_refs=[],
        trust_verdict=TrustVerdict.TRUSTED,
        lineage_hash="def",
    )

    diff = engine.compare(m1, m2)
    assert len(diff.semantic_deltas) == 2
    assert "size_change_i1" in diff.semantic_deltas
    assert "new_intent_i2" in diff.semantic_deltas
