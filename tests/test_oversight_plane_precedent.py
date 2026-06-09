def test_precedent_init():
    import app.oversight_plane.precedent as mod
    assert hasattr(mod, "initialize_precedent")
    assert mod.initialize_precedent() == "precedent initialized"
