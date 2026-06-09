def test_capture_init():
    import app.oversight_plane.capture as mod
    assert hasattr(mod, "initialize_capture")
    assert mod.initialize_capture() == "capture initialized"
