from app.drift_plane.models import DriftDebtRecord
from typing import Dict

class DebtManager:
    def __init__(self):
        self.debts: Dict[str, DriftDebtRecord] = {}

    def add_debt(self, debt_id: str, debt_type: str, severity: str):
        self.debts[debt_id] = DriftDebtRecord(
            debt_id=debt_id,
            debt_type=debt_type,
            severity=severity
        )

    def get_debt(self, debt_id: str) -> DriftDebtRecord:
        return self.debts.get(debt_id)
