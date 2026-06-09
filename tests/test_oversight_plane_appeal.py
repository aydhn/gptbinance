def test_appeal_init():
    import app.oversight_plane.appeal as mod
    assert hasattr(mod, "initialize_appeal")
    assert mod.initialize_appeal() == "appeal initialized"
