from datetime import datetime, timezone
from app.analytics.anomalies import AnomalyDetector
from app.analytics.models import AnalyticsRun, AnalyticsConfig
from app.analytics.enums import AnalyticsScope


def test_anomalies():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )
    detector = AnomalyDetector()
    res = detector.detect(run, [])

    # Mock currently returns empty, so we just assert no error and type
    assert isinstance(res, list)
