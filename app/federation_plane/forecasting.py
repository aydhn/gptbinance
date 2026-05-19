from typing import Dict, List, Optional
from app.federation_plane.models import FederationForecastReport
from app.federation_plane.exceptions import FederationPlaneError


class ForecastManager:
    def __init__(self):
        self._forecasts: Dict[str, FederationForecastReport] = {}

    def register(self, record: FederationForecastReport):
        if not record.forecast_id or not record.uncertainty_classes:
            raise FederationPlaneError("No fake predictive certainty allowed.")
        self._forecasts[record.forecast_id] = record

    def get_forecast(self, forecast_id: str) -> Optional[FederationForecastReport]:
        return self._forecasts.get(forecast_id)

    def list_forecasts(self) -> List[FederationForecastReport]:
        return list(self._forecasts.values())
