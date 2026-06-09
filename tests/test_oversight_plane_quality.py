def test_quality_init():
    import app.oversight_plane.quality as mod
    assert hasattr(mod, "initialize_quality")
    assert mod.initialize_quality() == "quality initialized"
