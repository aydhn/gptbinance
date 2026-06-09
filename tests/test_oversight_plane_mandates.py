def test_mandates_init():
    import app.oversight_plane.mandates as mod
    assert hasattr(mod, "initialize_mandates")
    assert mod.initialize_mandates() == "mandates initialized"
