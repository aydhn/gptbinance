def test_security_init():
    import app.oversight_plane.security as mod
    assert hasattr(mod, "initialize_security")
    assert mod.initialize_security() == "security initialized"
