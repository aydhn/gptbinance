from app.cost_plane.releases import ReleaseLinkage
def test_release_linkage():
    linkage = ReleaseLinkage()
    assert linkage.get_rollout_amplification_cost()["canary_cost"] == 100
