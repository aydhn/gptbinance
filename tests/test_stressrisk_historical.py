from app.stressrisk.historical import HistoricalStressLibrary


def test_historical_library():
    lib = HistoricalStressLibrary()
    scenario = lib.load_preset("march_2020_covid")
    assert scenario.scenario_id == "historical_march_2020"
