from app.stressrisk.derivatives import DerivativesStressEngine


def test_derivatives_engine():
    engine = DerivativesStressEngine()
    snapshot = engine.evaluate({})
    assert snapshot.total_funding_burden_jump == 500.0
