def test_repository_init():
    import app.oversight_plane.repository as mod
    assert hasattr(mod, "initialize_repository")
    assert mod.initialize_repository() == "repository initialized"
