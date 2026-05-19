from typing import Dict, List, Optional
from app.federation_plane.models import FederationDebtRecord
from app.federation_plane.exceptions import FederationPlaneError


class DebtManager:
    def __init__(self):
        self._debts: Dict[str, FederationDebtRecord] = {}

    def register(self, record: FederationDebtRecord):
        if not record.debt_id:
            raise FederationPlaneError("No silent debt burial allowed.")
        self._debts[record.debt_id] = record

    def get_debt(self, debt_id: str) -> Optional[FederationDebtRecord]:
        return self._debts.get(debt_id)

    def list_debts(self) -> List[FederationDebtRecord]:
        return list(self._debts.values())
