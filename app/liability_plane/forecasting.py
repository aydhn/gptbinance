import uuid
from app.liability_plane.models import LiabilityForecastReport
from app.liability_plane.repository import LiabilityRepository

class ForecastManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def create_forecast(self, liability_id: str, growth: str, risk: str, uncertainty: str) -> LiabilityForecastReport:
        return LiabilityForecastReport(
            forecast_id=str(uuid.uuid4()),
            liability_id=liability_id,
            exposure_growth_forecast=growth,
            indemnity_failure_risk=risk,
            uncertainty_class=uncertainty
        )
