def test_supervisors_init():
    import app.oversight_plane.supervisors as mod
    assert hasattr(mod, "initialize_supervisors")
    assert mod.initialize_supervisors() == "supervisors initialized"
