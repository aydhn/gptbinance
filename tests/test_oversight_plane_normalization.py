def test_normalization_init():
    import app.oversight_plane.normalization as mod
    assert hasattr(mod, "initialize_normalization")
    assert mod.initialize_normalization() == "normalization initialized"
