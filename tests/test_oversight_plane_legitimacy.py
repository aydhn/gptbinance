def test_legitimacy_init():
    import app.oversight_plane.legitimacy as mod
    assert hasattr(mod, "initialize_legitimacy")
    assert mod.initialize_legitimacy() == "legitimacy initialized"
