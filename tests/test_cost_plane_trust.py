from app.cost_plane.trust import TrustManager
from app.cost_plane.enums import CostTrustVerdict

def test_trust():
    manager = TrustManager()
    metrics = {"unattributed_spend_ratio": 0.2}
    record = manager.evaluate(metrics)
    assert record.verdict == CostTrustVerdict.BLOCKED
