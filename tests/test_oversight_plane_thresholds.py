def test_thresholds_init():
    import app.oversight_plane.thresholds as mod
    assert hasattr(mod, "initialize_thresholds")
    assert mod.initialize_thresholds() == "thresholds initialized"
