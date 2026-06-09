def test_succession_init():
    import app.oversight_plane.succession as mod
    assert hasattr(mod, "initialize_succession")
    assert mod.initialize_succession() == "succession initialized"
