def test_forecasting_init():
    import app.oversight_plane.forecasting as mod
    assert hasattr(mod, "initialize_forecasting")
    assert mod.initialize_forecasting() == "forecasting initialized"
