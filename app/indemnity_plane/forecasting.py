from app.indemnity_plane.models import IndemnityForecastReport
def generate_forecast(report_id: str) -> IndemnityForecastReport:
    return IndemnityForecastReport(report_id=report_id, forecasts=[])
