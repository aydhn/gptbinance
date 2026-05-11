from app.compliance_plane.models import ComplianceDebtRecord
from typing import Dict, List


class DebtManager:
    def __init__(self):
        self._debts: Dict[str, ComplianceDebtRecord] = {}

    def register_debt(self, debt: ComplianceDebtRecord) -> None:
        self._debts[debt.debt_id] = debt

    def list_debts(self) -> List[ComplianceDebtRecord]:
        return list(self._debts.values())
