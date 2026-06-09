def test_liability_init():
    import app.oversight_plane.liability as mod
    assert hasattr(mod, "initialize_liability")
    assert mod.initialize_liability() == "liability initialized"
