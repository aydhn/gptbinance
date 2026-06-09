def test_autonomy_init():
    import app.oversight_plane.autonomy as mod
    assert hasattr(mod, "initialize_autonomy")
    assert mod.initialize_autonomy() == "autonomy initialized"
