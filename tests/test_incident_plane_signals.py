from app.incident_plane.signals import IncidentSignalIntake

def test_signal_intake_correctness():
    alert = IncidentSignalIntake.ingest_alert("123", {"key": "val"})
    assert alert.signal_id == "SIG-ALERT-123"
    assert alert.source_system == "observability_alerts"
    assert alert.confidence_score == 0.8
    assert alert.raw_payload == {"key": "val"}

    anomaly = IncidentSignalIntake.ingest_anomaly("456", {"metric": "latency"})
    assert anomaly.signal_id == "SIG-ANOMALY-456"
    assert anomaly.source_system == "anomaly_detection"
    assert anomaly.confidence_score == 0.6
