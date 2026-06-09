def test_tradeoff_init():
    import app.oversight_plane.tradeoff as mod
    assert hasattr(mod, "initialize_tradeoff")
    assert mod.initialize_tradeoff() == "tradeoff initialized"
