def test_continuous_init():
    import app.oversight_plane.continuous as mod
    assert hasattr(mod, "initialize_continuous")
    assert mod.initialize_continuous() == "continuous initialized"
