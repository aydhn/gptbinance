def test_scope_init():
    import app.oversight_plane.scope as mod
    assert hasattr(mod, "initialize_scope")
    assert mod.initialize_scope() == "scope initialized"
