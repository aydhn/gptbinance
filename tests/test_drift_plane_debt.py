import pytest
from app.drift_plane.debt import DebtManager

def test_debt_creation():
    manager = DebtManager()
    manager.add_debt("debt-1", "hidden_drift", "critical")

    debt = manager.get_debt("debt-1")
    assert debt is not None
    assert debt.debt_id == "debt-1"
    assert debt.debt_type == "hidden_drift"
    assert debt.severity == "critical"
