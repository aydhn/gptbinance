from app.cost_plane.budgets import BudgetManager
from app.cost_plane.enums import BudgetClass

def test_budget_definition():
    manager = BudgetManager()
    budget = manager.define_budget("c-1", BudgetClass.HARD, "owner1", 1000.0, "USD", "monthly")
    assert budget.limit == 1000.0
