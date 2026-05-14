from app.cost_plane.models import BudgetDefinition, BudgetSnapshot
from app.cost_plane.enums import BudgetClass
from app.cost_plane.exceptions import InvalidBudgetDefinitionError
import uuid

class BudgetManager:
    def __init__(self):
        self._budgets: dict[str, BudgetDefinition] = {}
        self._snapshots: list[BudgetSnapshot] = []

    def define_budget(self, cost_id: str, budget_class: BudgetClass, owner: str, limit: float, currency: str, time_window: str) -> BudgetDefinition:
        budget = BudgetDefinition(
            budget_id=str(uuid.uuid4()),
            cost_id=cost_id,
            budget_class=budget_class,
            owner=owner,
            limit=limit,
            currency=currency,
            time_window=time_window
        )
        self._budgets[budget.budget_id] = budget
        return budget

    def record_snapshot(self, budget_id: str, spent: float) -> BudgetSnapshot:
        if budget_id not in self._budgets:
            raise InvalidBudgetDefinitionError("Budget not found")
        budget = self._budgets[budget_id]
        remaining = budget.limit - spent
        exhausted = remaining <= 0
        snapshot = BudgetSnapshot(
            budget_id=budget_id,
            spent=spent,
            remaining=remaining,
            exhausted=exhausted
        )
        self._snapshots.append(snapshot)
        return snapshot

    def list_budgets(self) -> list[BudgetDefinition]:
        return list(self._budgets.values())
