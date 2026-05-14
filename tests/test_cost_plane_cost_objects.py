from app.cost_plane.cost_objects import CostObjectManager

def test_create_direct_cost():
    obj = CostObjectManager.create_direct_cost("c-1", "owner1", "dev", "semantic", "weekly", "compute_spend")
    assert obj.cost_id == "c-1"
