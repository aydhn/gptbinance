from app.cost_plane.debt import CostDebtManager

def test_cost_debt():
    manager = CostDebtManager()
    record = manager.record_debt("c-1", "Stale reservation", "high", 1000.0, "USD")
    assert record.amount == 1000.0
