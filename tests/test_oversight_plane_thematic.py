def test_thematic_init():
    import app.oversight_plane.thematic as mod
    assert hasattr(mod, "initialize_thematic")
    assert mod.initialize_thematic() == "thematic initialized"
