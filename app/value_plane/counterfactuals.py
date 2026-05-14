from typing import Dict, List, Optional
from app.value_plane.models import CounterfactualBaseline

class CounterfactualRegistry:
    def __init__(self):
        self._records: Dict[str, CounterfactualBaseline] = {}

    def register(self, record: CounterfactualBaseline):
        self._records[record.counterfactual_id] = record

    def get(self, record_id: str) -> Optional[CounterfactualBaseline]:
        return self._records.get(record_id)

    def list_all(self) -> List[CounterfactualBaseline]:
        return list(self._records.values())

counterfactual_registry = CounterfactualRegistry()
