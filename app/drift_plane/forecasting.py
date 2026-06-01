from app.drift_plane.models import DriftForecastReport

class ForecastingManager:
    def create_forecast(self, forecast_type: str, uncertainty_class: str, details: str) -> DriftForecastReport:
        return DriftForecastReport(
            forecast_type=forecast_type,
            uncertainty_class=uncertainty_class,
            details=details
        )
