def test_directives_init():
    import app.oversight_plane.directives as mod
    assert hasattr(mod, "initialize_directives")
    assert mod.initialize_directives() == "directives initialized"
