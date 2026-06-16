from app.waterfall_plane.models import WaterfallForecastReport

def register_forecast(forecast_id: str, predictions: dict) -> WaterfallForecastReport:
    return WaterfallForecastReport(forecast_id=forecast_id, predictions=predictions)
