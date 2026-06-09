def test_exception_init():
    import app.oversight_plane.exception as mod
    assert hasattr(mod, "initialize_exception")
    assert mod.initialize_exception() == "exception initialized"
