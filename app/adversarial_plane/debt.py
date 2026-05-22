from typing import List, Optional
from app.adversarial_plane.models import AdversarialDebtRecord

def create_debt(debt_id: str, debt_type: str, severity: str, interest: str) -> AdversarialDebtRecord:
    valid_types = {"bypassable_control", "hidden_gaming", "stale_suspicion", "normalized_exploit", "review_evasion"}
    if debt_type not in valid_types:
        raise ValueError(f"Invalid debt type. Must be one of {valid_types}")
    return AdversarialDebtRecord(
        debt_id=debt_id,
        debt_type=debt_type,
        severity=severity,
        interest=interest
    )

class DebtManager:
    def __init__(self):
        self._debts = {}

    def add_debt(self, debt: AdversarialDebtRecord):
        self._debts[debt.debt_id] = debt

    def get_debt(self, debt_id: str) -> Optional[AdversarialDebtRecord]:
        return self._debts.get(debt_id)

    def list_debts(self) -> List[AdversarialDebtRecord]:
        return list(self._debts.values())
