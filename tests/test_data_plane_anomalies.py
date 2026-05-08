from app.data_plane.anomalies import AnomalyDetector


def test_anomaly_detector():
    detector = AnomalyDetector()
    finding = detector.detect_timestamp_skew(1000.0, 3000.0, 1000)
    assert finding is not None
    assert finding.anomaly_id == "skew_1000.0_3000.0"

    finding2 = detector.detect_timestamp_skew(1000.0, 1500.0, 1000)
    assert finding2 is None
