import pytest

from app.reliability_plane.budgets import ErrorBudgetManager
from app.reliability_plane.enums import BudgetClass
from app.reliability_plane.exceptions import InvalidBudgetPolicy
from app.reliability_plane.models import ErrorBudgetPolicy


def test_budget_threshold_logic():
    manager = ErrorBudgetManager()
    with pytest.raises(InvalidBudgetPolicy):
        policy = ErrorBudgetPolicy(
            policy_id="p1",
            slo_id="s1",
            budget_class=BudgetClass.STRICT,
            depletion_threshold_alert=0.9,
            freeze_threshold=0.5,
            reset_policy_notes="",
        )
        manager.register_policy(policy)
