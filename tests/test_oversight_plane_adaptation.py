def test_adaptation_init():
    import app.oversight_plane.adaptation as mod
    assert hasattr(mod, "initialize_adaptation")
    assert mod.initialize_adaptation() == "adaptation initialized"
