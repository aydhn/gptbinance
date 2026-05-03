from app.perf.budgets import BudgetRegistry
from app.perf.enums import ResourceType, BudgetSeverity
from app.perf.models import ResourceBudget


def test_budget_registry():
    r = BudgetRegistry.get_applicable_resource_budgets("paper")
    assert len(r) > 0
    assert any(b.resource_type == ResourceType.MEMORY for b in r)
