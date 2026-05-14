from typing import Dict, List, Optional
from app.value_plane.models import ValuePortfolioRollup

class PortfolioRegistry:
    def __init__(self):
        self._records: Dict[str, ValuePortfolioRollup] = {}

    def register(self, record: ValuePortfolioRollup):
        self._records[record.rollup_id] = record

    def get(self, record_id: str) -> Optional[ValuePortfolioRollup]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValuePortfolioRollup]:
        return list(self._records.values())

portfolio_registry = PortfolioRegistry()
