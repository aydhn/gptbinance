def test_renewal_init():
    import app.oversight_plane.renewal as mod
    assert hasattr(mod, "initialize_renewal")
    assert mod.initialize_renewal() == "renewal initialized"
