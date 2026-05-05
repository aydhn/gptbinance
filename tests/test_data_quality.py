from app.data_governance import QualityEngine, DatasetRef, DatasetType, TrustLevel
from datetime import datetime, timezone


def test_quality_engine_evaluation():
    engine = QualityEngine()
    ref = DatasetRef(
        dataset_id="d1", dataset_type=DatasetType.RAW_MARKET_DATA, version="v1"
    )
    report = engine.evaluate(ref, data=[])

    assert report.dataset_ref.dataset_id == "d1"
    assert len(report.results) > 0
    # The mock returns passed=True for duplicate keys, so status should be TRUSTED
    assert report.status == TrustLevel.TRUSTED
    assert report.overall_score == 1.0
