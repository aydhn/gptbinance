def test_representation_init():
    import app.oversight_plane.representation as mod
    assert hasattr(mod, "initialize_representation")
    assert mod.initialize_representation() == "representation initialized"
