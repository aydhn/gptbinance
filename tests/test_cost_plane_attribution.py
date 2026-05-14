from app.cost_plane.attribution import AttributionManager

def test_attribution_manager():
    manager = AttributionManager()
    record = manager.record_attribution("spend-1", "workload-a", "live")
    assert record["completeness"] == 1.0
