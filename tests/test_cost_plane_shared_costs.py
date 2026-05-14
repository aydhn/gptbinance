from app.cost_plane.shared_costs import SharedCostManager

def test_shared_cost_pool():
    manager = SharedCostManager()
    pool = manager.create_pool("platform-pool", 5000.0, "USD", "policy-1")
    assert pool.total_amount == 5000.0
