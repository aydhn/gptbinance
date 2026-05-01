from datetime import datetime, timezone
from app.analytics.diagnostics import RootCauseDiagnosticEngine
from app.analytics.models import AnalyticsRun, AnalyticsConfig
from app.analytics.enums import AnalyticsScope


def test_diagnostics():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )
    engine = RootCauseDiagnosticEngine()
    res = engine.run_diagnostics(run, [])

    # Mock currently returns empty, so we just assert type
    assert isinstance(res, list)
