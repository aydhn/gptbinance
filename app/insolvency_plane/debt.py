# debt.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import InsolvencyDebtRecord

class InsolvencyDebtManager:
    def __init__(self):
        self.debts: Dict[str, InsolvencyDebtRecord] = {}

    def register_debt(self, debt: InsolvencyDebtRecord):
        self.debts[debt.debt_id] = debt

    def get_debt(self, debt_id: str) -> Optional[InsolvencyDebtRecord]:
        return self.debts.get(debt_id)

    def list_debts(self) -> List[InsolvencyDebtRecord]:
        return list(self.debts.values())
