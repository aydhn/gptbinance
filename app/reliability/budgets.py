from typing import Dict, List
import uuid
from app.reliability.enums import BudgetClass
from app.reliability.models import ErrorBudget, ErrorBudgetConsumption
from app.reliability.exceptions import InvalidErrorBudget, ReliabilityTowerError


class ErrorBudgetRegistry:
    def __init__(self):
        self._budgets: Dict[str, ErrorBudget] = {}
        self._consumptions: Dict[str, List[ErrorBudgetConsumption]] = {}

    def register(self, budget: ErrorBudget):
        if budget.budget_id in self._budgets:
            raise InvalidErrorBudget(f"Budget {budget.budget_id} already registered.")
        if budget.total_budget_value <= 0:
            raise InvalidErrorBudget(f"Budget total value must be > 0.")
        self._budgets[budget.budget_id] = budget
        self._consumptions[budget.budget_id] = []

    def get(self, budget_id: str) -> ErrorBudget:
        if budget_id not in self._budgets:
            raise ReliabilityTowerError(f"Budget {budget_id} not found.")
        return self._budgets[budget_id]

    def consume(
        self, budget_id: str, value: float, rationale: str
    ) -> ErrorBudgetConsumption:
        budget = self.get(budget_id)
        if value < 0:
            raise ReliabilityTowerError("Consumption value cannot be negative.")

        consumption = ErrorBudgetConsumption(
            consumption_id=f"cons_{uuid.uuid4().hex[:8]}",
            budget_id=budget_id,
            consumed_value=value,
            rationale=rationale,
        )

        budget.remaining_budget -= value

        # Soft budget exhaustion allows negative remaining, hard budget might trigger stronger alerts later
        if budget.remaining_budget < 0 and budget.budget_class == BudgetClass.HARD:
            # In a real system, this might trigger a hard freeze immediately.
            # As per requirements: "error budget tükenmesi otomatik action değil; açık recommendation ve gating input üretecek."
            pass

        self._consumptions[budget_id].append(consumption)
        return consumption

    def list_consumptions(self, budget_id: str) -> List[ErrorBudgetConsumption]:
        return self._consumptions.get(budget_id, [])

    def reset(self, budget_id: str):
        budget = self.get(budget_id)
        budget.remaining_budget = budget.total_budget_value
        # Consumptions are kept for historical trend analysis


budget_registry = ErrorBudgetRegistry()
