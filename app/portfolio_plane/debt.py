from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioDebtRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class DebtManager:
    def __init__(self):
        self._records: Dict[str, PortfolioDebtRecord] = {}

    def register(self, record: PortfolioDebtRecord):
        if record.debt_id in self._records:
            raise PortfolioStorageError(f"Debt {record.debt_id} already exists")
        self._records[record.debt_id] = record

    def get(self, record_id: str) -> Optional[PortfolioDebtRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, PortfolioDebtRecord]:
        return self._records.copy()
