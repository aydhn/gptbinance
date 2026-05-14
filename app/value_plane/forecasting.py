from typing import Dict, List, Optional
from app.value_plane.models import ValueForecastReport

class ForecastRegistry:
    def __init__(self):
        self._records: Dict[str, ValueForecastReport] = {}

    def register(self, record: ValueForecastReport):
        self._records[record.forecast_id] = record

    def get(self, record_id: str) -> Optional[ValueForecastReport]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValueForecastReport]:
        return list(self._records.values())

forecast_registry = ForecastRegistry()
