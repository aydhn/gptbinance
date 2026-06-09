def test_viability_init():
    import app.oversight_plane.viability as mod
    assert hasattr(mod, "initialize_viability")
    assert mod.initialize_viability() == "viability initialized"
