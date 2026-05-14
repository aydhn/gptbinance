import pytest
from app.cost_plane.registry import CanonicalCostRegistry
from app.cost_plane.cost_objects import CostObjectManager
from app.cost_plane.exceptions import InvalidCostObjectError

def test_registry_register_and_get():
    registry = CanonicalCostRegistry()
    cost_obj = CostObjectManager.create_direct_cost("c-1", "team-a", "live", "direct", "monthly", "compute_spend")
    registry.register_cost(cost_obj)
    retrieved = registry.get_cost("c-1")
    assert retrieved.cost_id == "c-1"

def test_registry_invalid_family():
    registry = CanonicalCostRegistry()
    cost_obj = CostObjectManager.create_direct_cost("c-2", "team-a", "live", "direct", "monthly", "invalid_family")
    with pytest.raises(InvalidCostObjectError):
        registry.register_cost(cost_obj)
