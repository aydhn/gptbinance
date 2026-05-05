from app.market_truth.storage import MarketTruthStorage
from app.market_truth.repository import MarketTruthRepository
from app.market_truth.models import MarketTruthAuditRecord, MarketTruthEvidenceBundle
from datetime import datetime, timezone


def test_storage():
    st = MarketTruthStorage()
    repo = MarketTruthRepository(st)
    bundle = MarketTruthEvidenceBundle(
        timestamp=datetime.now(timezone.utc),
        symbol="BTC",
        verdicts=[],
        overall_verdict="ALLOW",
    )
    rec = MarketTruthAuditRecord(
        run_id="r1", timestamp=datetime.now(timezone.utc), evidence_bundle=bundle
    )
    st.save_audit_record(rec)
    res = repo.get_latest_truthfulness("BTC")
    assert res is not None
