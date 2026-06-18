from typing import Dict, Any
from .models import NettingForecastReport

class ForecastingManager:
    def __init__(self):
        self.reports: Dict[str, NettingForecastReport] = {}

    def generate_report(self, data: Dict[str, Any]) -> NettingForecastReport:
        rep = NettingForecastReport(**data)
        self.reports[rep.forecast_id] = rep
        return rep
