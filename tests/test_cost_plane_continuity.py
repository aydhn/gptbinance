from app.cost_plane.continuity import ContinuityLinkage
def test_continuity_linkage():
    linkage = ContinuityLinkage()
    assert linkage.evaluate_dr_investment()["standby_cost_posture"] == "funded"
