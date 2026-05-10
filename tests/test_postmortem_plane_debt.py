import pytest
from app.postmortem_plane.debt import RemediationDebtTracker
from app.postmortem_plane.enums import DebtClass, DebtInterestClass

def test_debt_tracker():
    debt = RemediationDebtTracker.track_debt("D-1", "A-1", DebtClass.OVERDUE, DebtInterestClass.CRITICAL)
    assert debt.debt_id == "D-1"
    assert debt.interest_class == DebtInterestClass.CRITICAL
