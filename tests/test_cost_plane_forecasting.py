from app.cost_plane.forecasting import ForecastManager
from app.cost_plane.spend import SpendManager
from app.cost_plane.enums import SpendClass

def test_forecast():
    spend_mgr = SpendManager()
    spend_mgr.record_spend("c-1", SpendClass.ACTUAL, 100.0, "USD")
    manager = ForecastManager()
    report = manager.evaluate(spend_mgr.list_records())
    assert report.forecast_amount > 0
