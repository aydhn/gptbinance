def test_readiness_init():
    import app.oversight_plane.readiness as mod
    assert hasattr(mod, "initialize_readiness")
    assert mod.initialize_readiness() == "readiness initialized"
