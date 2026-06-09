def test_triggers_init():
    import app.oversight_plane.triggers as mod
    assert hasattr(mod, "initialize_triggers")
    assert mod.initialize_triggers() == "triggers initialized"
