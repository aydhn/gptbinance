from app.reliability.budgets import ErrorBudgetRegistry
from app.reliability.models import ErrorBudget
from app.reliability.enums import BudgetClass
from app.reliability.exceptions import InvalidErrorBudget


def test_error_budget_consumption():
    registry = ErrorBudgetRegistry()
    budget = ErrorBudget(
        budget_id="b1",
        slo_id="s1",
        budget_class=BudgetClass.HARD,
        total_budget_value=100.0,
        remaining_budget=100.0,
    )
    registry.register(budget)

    consumption = registry.consume("b1", 10.0, "Test consume")
    assert consumption.consumed_value == 10.0

    b = registry.get("b1")
    assert b.remaining_budget == 90.0
