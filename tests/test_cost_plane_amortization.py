from app.cost_plane.amortization import AmortizationManager
from app.cost_plane.enums import AmortizationClass

def test_amortization():
    manager = AmortizationManager()
    record = manager.record_amortization("c-1", AmortizationClass.RESERVED_CAPACITY, 12000.0, 1000.0, "USD")
    assert record.amortized_amount_per_period == 1000.0
