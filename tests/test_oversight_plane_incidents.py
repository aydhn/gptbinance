def test_incidents_init():
    import app.oversight_plane.incidents as mod
    assert hasattr(mod, "initialize_incidents")
    assert mod.initialize_incidents() == "incidents initialized"
