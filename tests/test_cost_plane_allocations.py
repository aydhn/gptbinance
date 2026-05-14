from app.cost_plane.allocations import AllocationManager
from app.cost_plane.enums import AllocationClass
from app.cost_plane.spend import SpendManager
from app.cost_plane.enums import SpendClass

def test_allocations():
    manager = AllocationManager()
    spend_mgr = SpendManager()
    spend_record = spend_mgr.record_spend("c-1", SpendClass.ACTUAL, 1000.0, "USD")
    policy = manager.define_policy(AllocationClass.DIRECT, {"target": "workload-a"}, ["ref1"])
    records = manager.evaluate(policy, spend_record)
    assert records[0].allocated_to == "workload-a"
