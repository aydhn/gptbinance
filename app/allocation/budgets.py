from typing import Dict, List
from app.allocation.models import SleeveBudget
from app.allocation.enums import BudgetClass
from app.allocation.exceptions import InvalidBudget


class BudgetManager:
    def __init__(self):
        self._budgets: Dict[str, SleeveBudget] = {}
        self._init_defaults()

    def _init_defaults(self):
        self._budgets["primary_alpha_01"] = SleeveBudget(
            sleeve_id="primary_alpha_01",
            budget_class=BudgetClass.CORE,
            allocated_notional=100000.0,
            consumed_notional=0.0,
            headroom=100000.0,
            is_frozen=False,
        )
        self._budgets["hedge_overlay_01"] = SleeveBudget(
            sleeve_id="hedge_overlay_01",
            budget_class=BudgetClass.DEFENSIVE,
            allocated_notional=50000.0,
            consumed_notional=0.0,
            headroom=50000.0,
            is_frozen=False,
        )

    def get_budget(self, sleeve_id: str) -> SleeveBudget:
        if sleeve_id not in self._budgets:
            raise InvalidBudget(f"Budget for sleeve {sleeve_id} not found")
        return self._budgets[sleeve_id]

    def consume(self, sleeve_id: str, amount: float):
        b = self.get_budget(sleeve_id)
        if b.is_frozen:
            raise InvalidBudget(f"Sleeve {sleeve_id} is frozen, cannot allocate")
        if b.headroom < amount:
            raise InvalidBudget(f"Insufficient headroom in sleeve {sleeve_id}")
        b.consumed_notional += amount
        b.headroom -= amount

    def get_all_budgets(self) -> List[SleeveBudget]:
        return list(self._budgets.values())
