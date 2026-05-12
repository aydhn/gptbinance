import pytest
from app.observability_plane.anomalies import AnomalyDetectorRegistry
from app.observability_plane.models import TelemetryAnomalyFinding

def test_anomaly_reporting():
    reg = AnomalyDetectorRegistry()
    reg.report_anomaly(TelemetryAnomalyFinding(anomaly_id="a1", telemetry_id="t1", anomaly_type="spike"))
    assert reg.get_anomaly("a1").anomaly_type == "spike"
