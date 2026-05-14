from app.cost_plane.unit_economics import UnitEconomicsManager
from app.cost_plane.enums import UnitEconomicsClass

def test_unit_economics():
    manager = UnitEconomicsManager()
    record = manager.record_economics("c-1", UnitEconomicsClass.PER_ORDER, 0.05, "USD", "High confidence")
    assert record.unit_cost == 0.05
