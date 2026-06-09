def test_temporal_init():
    import app.oversight_plane.temporal as mod
    assert hasattr(mod, "initialize_temporal")
    assert mod.initialize_temporal() == "temporal initialized"
