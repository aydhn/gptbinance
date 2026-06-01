from app.assurance_plane.models import AssuranceForecastReport

def create_forecast(forecast_id: str, expiry_risk: str, contradiction_emergence: str, surveillance_decay: str) -> AssuranceForecastReport:
    return AssuranceForecastReport(
        forecast_id=forecast_id,
        expiry_risk=expiry_risk,
        contradiction_emergence=contradiction_emergence,
        surveillance_decay=surveillance_decay
    )
