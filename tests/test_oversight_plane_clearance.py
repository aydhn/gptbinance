def test_clearance_init():
    import app.oversight_plane.clearance as mod
    assert hasattr(mod, "initialize_clearance")
    assert mod.initialize_clearance() == "clearance initialized"
