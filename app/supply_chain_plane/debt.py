from typing import Dict, Optional, List
from app.supply_chain_plane.models import SupplyChainDebtRecord


class DebtRegistry:
    def __init__(self):
        self._debts: Dict[str, SupplyChainDebtRecord] = {}

    def register_debt(self, debt: SupplyChainDebtRecord) -> None:
        self._debts[debt.debt_id] = debt

    def get_debt(self, debt_id: str) -> Optional[SupplyChainDebtRecord]:
        return self._debts.get(debt_id)

    def get_debts_for_component(self, component_id: str) -> List[SupplyChainDebtRecord]:
        return [
            d
            for d in self._debts.values()
            if d.component_ref.component_id == component_id
        ]
