def test_oversight_init():
    import app.oversight_plane.oversight as mod
    assert hasattr(mod, "initialize_oversight")
    assert mod.initialize_oversight() == "oversight initialized"
