def test_drift_integration_init():
    import app.oversight_plane.drift_integration as mod
    assert hasattr(mod, "initialize_drift_integration")
    assert mod.initialize_drift_integration() == "drift_integration initialized"
