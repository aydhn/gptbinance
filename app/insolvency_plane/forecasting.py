# forecasting.py
from typing import Dict, List, Optional
from pydantic import BaseModel
from app.insolvency_plane.models import InsolvencyObjectRef

class InsolvencyForecastReport(BaseModel):
    forecast_id: str
    insolvency_ref: InsolvencyObjectRef
    forecast_type: str # leakage_risk, impairment_growth, plan_failure, liquidation_deficiency, stay_bypass_risk
    uncertainty_class: str
    description: str
    lineage_refs: List[str]

class InsolvencyForecastManager:
    def __init__(self):
        self.forecasts: Dict[str, InsolvencyForecastReport] = {}

    def register_forecast(self, forecast: InsolvencyForecastReport):
        self.forecasts[forecast.forecast_id] = forecast

    def get_forecast(self, forecast_id: str) -> Optional[InsolvencyForecastReport]:
        return self.forecasts.get(forecast_id)

    def list_forecasts(self) -> List[InsolvencyForecastReport]:
        return list(self.forecasts.values())
