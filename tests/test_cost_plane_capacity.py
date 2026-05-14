from app.cost_plane.capacity import CapacityLinkage
def test_capacity_linkage():
    linkage = CapacityLinkage()
    assert linkage.map_usage_to_spend("res-1")["spend_mapping"] == "ok"
