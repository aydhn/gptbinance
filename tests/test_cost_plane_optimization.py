from app.cost_plane.optimization import OptimizationManager

def test_optimization():
    manager = OptimizationManager()
    record = manager.record_opportunity("c-1", "Right size DB", 500.0, "USD", ["Could impact latency"])
    assert record.estimated_savings == 500.0
