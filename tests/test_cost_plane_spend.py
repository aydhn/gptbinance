from app.cost_plane.spend import SpendManager
from app.cost_plane.enums import SpendClass

def test_spend_manager_record():
    manager = SpendManager()
    record = manager.record_spend("c-1", SpendClass.ACTUAL, 100.0, "USD")
    assert record.amount == 100.0
