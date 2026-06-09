def test_divergence_init():
    import app.oversight_plane.divergence as mod
    assert hasattr(mod, "initialize_divergence")
    assert mod.initialize_divergence() == "divergence initialized"
