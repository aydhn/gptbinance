from app.stressrisk.correlation import CorrelationStressEngine


def test_correlation_engine():
    engine = CorrelationStressEngine()
    snapshot = engine.evaluate({}, {})
    assert snapshot.average_correlation_jump == 0.4
    assert len(snapshot.highly_correlated_clusters) > 0
