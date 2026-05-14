from app.cost_plane.usage_costs import UsageCostManager

def test_usage_costs():
    manager = UsageCostManager()
    record = manager.record_usage("c-1", 0.5, 1000.0, "USD")
    assert record.total_cost == 500.0
