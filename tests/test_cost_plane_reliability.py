from app.cost_plane.reliability import ReliabilityLinkage
def test_reliability_linkage():
    linkage = ReliabilityLinkage()
    assert linkage.evaluate_cost_vs_reliability(100.0, 0.6) == "caution_cheap_but_fragile"
