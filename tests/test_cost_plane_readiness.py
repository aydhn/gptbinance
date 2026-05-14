from app.cost_plane.readiness import CostReadinessAggregation
def test_readiness_aggregation():
    cra = CostReadinessAggregation()
    assert cra.evaluate_readiness()["budget_hygiene"] == "ok"
