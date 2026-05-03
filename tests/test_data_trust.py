from app.data_governance import TrustVerdictEngine, DatasetRef, DatasetType, DatasetQualityReport, TrustLevel, QualityScoreBreakdown
from datetime import datetime, timezone

def test_trust_verdict_engine():
    engine = TrustVerdictEngine()
    ref = DatasetRef(dataset_id="d1", dataset_type=DatasetType.RAW_MARKET_DATA, version="v1")

    # Mock quality report
    qreport = DatasetQualityReport(
        dataset_ref=ref,
        run_id="run1",
        timestamp=datetime.now(timezone.utc),
        results=[],
        breakdown=QualityScoreBreakdown(total_rules=1, passed_rules=1, failed_critical=0, failed_high=0, failed_medium=0, failed_low=0),
        overall_score=1.0,
        status=TrustLevel.TRUSTED
    )

    verdict = engine.evaluate(ref, qreport, lineage_complete=True, canonical_confidence=True, schema_compatible=True)
    assert verdict.verdict == TrustLevel.TRUSTED

    verdict = engine.evaluate(ref, qreport, lineage_complete=False)
    assert verdict.verdict == TrustLevel.CAUTION

    verdict = engine.evaluate(ref, qreport, schema_compatible=False)
    assert verdict.verdict == TrustLevel.BLOCKED
