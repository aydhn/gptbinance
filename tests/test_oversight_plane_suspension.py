def test_suspension_init():
    import app.oversight_plane.suspension as mod
    assert hasattr(mod, "initialize_suspension")
    assert mod.initialize_suspension() == "suspension initialized"
