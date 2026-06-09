def test_reporting_init():
    import app.oversight_plane.reporting as mod
    assert hasattr(mod, "initialize_reporting")
    assert mod.initialize_reporting() == "reporting initialized"
