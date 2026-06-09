def test_accountability_init():
    import app.oversight_plane.accountability as mod
    assert hasattr(mod, "initialize_accountability")
    assert mod.initialize_accountability() == "accountability initialized"
