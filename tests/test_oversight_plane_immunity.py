def test_immunity_init():
    import app.oversight_plane.immunity as mod
    assert hasattr(mod, "initialize_immunity")
    assert mod.initialize_immunity() == "immunity initialized"
