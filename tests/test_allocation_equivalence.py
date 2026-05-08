from app.allocation.equivalence import EquivalenceEngine
from app.allocation.models import AllocationManifest, TrustVerdict
from app.allocation.enums import EquivalenceVerdict
from datetime import datetime, timezone


def test_equivalence():
    engine = EquivalenceEngine()
    m1 = AllocationManifest(
        manifest_id="m1",
        timestamp=datetime.now(timezone.utc),
        intents=[],
        portfolio_gross_exposure=10,
        portfolio_net_exposure=10,
        constraints_refs=[],
        trust_verdict=TrustVerdict.TRUSTED,
        lineage_hash="abc",
    )
    m2 = AllocationManifest(
        manifest_id="m2",
        timestamp=datetime.now(timezone.utc),
        intents=[],
        portfolio_gross_exposure=10,
        portfolio_net_exposure=10,
        constraints_refs=[],
        trust_verdict=TrustVerdict.TRUSTED,
        lineage_hash="abc",
    )
    m3 = AllocationManifest(
        manifest_id="m3",
        timestamp=datetime.now(timezone.utc),
        intents=[],
        portfolio_gross_exposure=20,
        portfolio_net_exposure=20,
        constraints_refs=[],
        trust_verdict=TrustVerdict.TRUSTED,
        lineage_hash="def",
    )

    assert engine.evaluate(m1, m2) == EquivalenceVerdict.EQUIVALENT
    assert engine.evaluate(m1, m3) == EquivalenceVerdict.DIVERGED_CRITICAL
