from typing import Dict, List, Optional
from .models import CardinalityCostRecord

class CardinalityTracker:
    def __init__(self):
        self._records: Dict[str, CardinalityCostRecord] = {}

    def report_cardinality(self, record: CardinalityCostRecord) -> None:
        self._records[record.telemetry_id] = record

    def get_cardinality(self, telemetry_id: str) -> Optional[CardinalityCostRecord]:
        return self._records.get(telemetry_id)

    def list_cardinality(self) -> List[CardinalityCostRecord]:
        return list(self._records.values())
