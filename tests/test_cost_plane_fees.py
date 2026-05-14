from app.cost_plane.fees import FeeManager
from app.cost_plane.enums import FeeClass

def test_fee_manager():
    manager = FeeManager()
    record = manager.record_fee("c-1", FeeClass.EXCHANGE_FEE, 5.0, "USD")
    assert record.amount == 5.0
