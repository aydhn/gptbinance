def test_finality_init():
    import app.oversight_plane.finality as mod
    assert hasattr(mod, "initialize_finality")
    assert mod.initialize_finality() == "finality initialized"
