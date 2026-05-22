from typing import List, Optional
from app.adversarial_plane.models import AdversarialForecastReport

def create_forecast(forecast_id: str, exploit_recurrence: str, gaming_incentive_growth: str, stealth_surface: str, control_erosion: str, uncertainty_classes: List[str]) -> AdversarialForecastReport:
    return AdversarialForecastReport(
        forecast_id=forecast_id,
        exploit_recurrence=exploit_recurrence,
        gaming_incentive_growth=gaming_incentive_growth,
        stealth_surface=stealth_surface,
        control_erosion=control_erosion,
        uncertainty_classes=uncertainty_classes
    )

class ForecastManager:
    def __init__(self):
        self._forecasts = {}

    def add_forecast(self, fc: AdversarialForecastReport):
        self._forecasts[fc.forecast_id] = fc

    def get_forecast(self, forecast_id: str) -> Optional[AdversarialForecastReport]:
        return self._forecasts.get(forecast_id)

    def list_forecasts(self) -> List[AdversarialForecastReport]:
        return list(self._forecasts.values())
