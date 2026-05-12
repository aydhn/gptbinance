import pytest
from app.observability_plane.correlation import CorrelationEngine
from app.observability_plane.models import TelemetryCorrelationReport

def test_correlation_engine():
    engine = CorrelationEngine()
    engine.report_correlation(TelemetryCorrelationReport(correlation_id="c1", telemetry_refs=["t1", "t2"], confidence_score=0.9))
    assert engine.get_correlation("c1").confidence_score == 0.9
