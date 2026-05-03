from app.stressrisk.enums import LossSeverity
from app.stressrisk.losses import LossEstimator


def test_loss_estimator():
    estimator = LossEstimator()
    est = estimator.estimate("s1", "BTC", 1000.0, 0.8)  # 20% drop
    assert est.estimated_loss == 200.0
    assert est.loss_severity == LossSeverity.CRITICAL
