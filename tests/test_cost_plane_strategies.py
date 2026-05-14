from app.cost_plane.strategies import StrategyLinkage
def test_strategy_linkage():
    linkage = StrategyLinkage()
    assert linkage.calculate_sustainability_posture()["strategy_unit_economics"] == "sustainable"
