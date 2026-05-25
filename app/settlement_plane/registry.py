from typing import Dict, List
from app.settlement_plane.models import SettlementRecord
from app.settlement_plane.enums import SettlementClass
from app.settlement_plane.exceptions import InvalidSettlementObjectError

class SettlementRegistry:
    def __init__(self):
        self._settlements: Dict[str, SettlementRecord] = {}

    def register(self, record: SettlementRecord) -> None:
        if record.id in self._settlements:
            raise InvalidSettlementObjectError(f"Settlement {record.id} already registered.")
        if not record.scope_refs:
             raise InvalidSettlementObjectError(f"Settlement {record.id} missing scope.")
        self._settlements[record.id] = record

    def get(self, settlement_id: str) -> SettlementRecord:
        if settlement_id not in self._settlements:
             raise InvalidSettlementObjectError(f"Settlement {settlement_id} not found.")
        return self._settlements[settlement_id]

    def list_all(self) -> List[SettlementRecord]:
        return list(self._settlements.values())
