def test_interpretation_init():
    import app.oversight_plane.interpretation as mod
    assert hasattr(mod, "initialize_interpretation")
    assert mod.initialize_interpretation() == "interpretation initialized"
