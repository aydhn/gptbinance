from app.performance_security_plane.models import SecurityForecastReport

class ForecastingManager:
    def create_forecast(self, forecast_id: str, security_id: str, forecast_type: str, uncertainty_class: str) -> SecurityForecastReport:
        return SecurityForecastReport(
            forecast_id=forecast_id,
            security_id=security_id,
            type=forecast_type,
            uncertainty_class=uncertainty_class
        )
