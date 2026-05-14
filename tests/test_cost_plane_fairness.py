from app.cost_plane.fairness import FairnessManager

def test_fairness():
    manager = FairnessManager()
    record = manager.evaluate_fairness(True, "live", "research", "high", "Live subsidizes research")
    assert record["subsidy_detected"]
