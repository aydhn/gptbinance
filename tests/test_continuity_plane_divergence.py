import pytest
from datetime import datetime, timezone
from app.continuity_plane.divergence import ContinuityDivergenceAnalyzer
from app.continuity_plane.models import ContinuityDivergenceReport

def test_divergence_analyzer():
    analyzer = ContinuityDivergenceAnalyzer()
    report = ContinuityDivergenceReport(
        service_id="srv_1",
        divergence_source="standby_drift",
        severity="medium",
        description="Schema mismatch",
        timestamp=datetime.now(timezone.utc)
    )
    analyzer.record_report(report)

    reports = analyzer.list_reports_for_service("srv_1")
    assert len(reports) == 1
    assert reports[0].divergence_source == "standby_drift"
