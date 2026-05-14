from app.cost_plane.variance import VarianceManager
from app.cost_plane.enums import VarianceClass

def test_variance():
    manager = VarianceManager()
    record = manager.record_variance("c-1", VarianceClass.BUDGET_VARIANCE, 1000.0, 1200.0, False)
    assert record.variance_amount == 200.0
