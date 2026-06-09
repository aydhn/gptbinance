def test_watchlists_init():
    import app.oversight_plane.watchlists as mod
    assert hasattr(mod, "initialize_watchlists")
    assert mod.initialize_watchlists() == "watchlists initialized"
