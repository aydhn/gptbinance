from typing import Dict, List, Optional
from app.value_plane.models import TradeoffRecord

class TradeoffRegistry:
    def __init__(self):
        self._records: Dict[str, TradeoffRecord] = {}

    def register(self, record: TradeoffRecord):
        self._records[record.tradeoff_id] = record

    def get(self, record_id: str) -> Optional[TradeoffRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[TradeoffRecord]:
        return list(self._records.values())

tradeoff_registry = TradeoffRegistry()
