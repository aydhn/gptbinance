from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityForecastReport

class ContinuityForecaster:
    def __init__(self):
        self._forecasts: Dict[str, ContinuityForecastReport] = {}

    def record_forecast(self, record: ContinuityForecastReport) -> None:
        self._forecasts[record.service_id] = record

    def get_forecast(self, service_id: str) -> Optional[ContinuityForecastReport]:
        return self._forecasts.get(service_id)

    def list_forecasts(self) -> List[ContinuityForecastReport]:
        return list(self._forecasts.values())
