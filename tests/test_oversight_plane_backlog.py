def test_backlog_init():
    import app.oversight_plane.backlog as mod
    assert hasattr(mod, "initialize_backlog")
    assert mod.initialize_backlog() == "backlog initialized"
