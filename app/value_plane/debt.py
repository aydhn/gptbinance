from typing import Dict, List, Optional
from app.value_plane.models import ValueDebtRecord

class DebtRegistry:
    def __init__(self):
        self._records: Dict[str, ValueDebtRecord] = {}

    def register(self, record: ValueDebtRecord):
        self._records[record.debt_id] = record

    def get(self, record_id: str) -> Optional[ValueDebtRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValueDebtRecord]:
        return list(self._records.values())

debt_registry = DebtRegistry()
