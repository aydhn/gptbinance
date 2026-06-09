def test_sunset_init():
    import app.oversight_plane.sunset as mod
    assert hasattr(mod, "initialize_sunset")
    assert mod.initialize_sunset() == "sunset initialized"
