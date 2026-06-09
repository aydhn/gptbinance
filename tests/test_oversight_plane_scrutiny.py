def test_scrutiny_init():
    import app.oversight_plane.scrutiny as mod
    assert hasattr(mod, "initialize_scrutiny")
    assert mod.initialize_scrutiny() == "scrutiny initialized"
