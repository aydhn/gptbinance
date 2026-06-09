def test_authority_init():
    import app.oversight_plane.authority as mod
    assert hasattr(mod, "initialize_authority")
    assert mod.initialize_authority() == "authority initialized"
