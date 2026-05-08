from app.allocation.reporting import ReportingEngine
from app.allocation.models import AllocationManifest, TrustVerdict
from datetime import datetime, timezone


def test_reporting():
    engine = ReportingEngine()
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
    summary = engine.generate_summary(m1)
    assert "Manifest: m1" in summary
    assert "Gross Exposure: 10" in summary
