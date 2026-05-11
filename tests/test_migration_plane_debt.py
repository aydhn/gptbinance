import pytest
from app.migration_plane.debt import DebtManager
from app.migration_plane.enums import DebtClass

def test_record_debt():
    manager = DebtManager()
    result = manager.record_debt("mig_001", DebtClass.SHIM_DEBT, "HIGH", {"note": "Fix later"})
    assert result.debt_class == DebtClass.SHIM_DEBT
    assert result.severity == "HIGH"
    assert result.is_resolved is False
