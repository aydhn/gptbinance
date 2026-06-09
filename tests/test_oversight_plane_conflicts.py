def test_conflicts_init():
    import app.oversight_plane.conflicts as mod
    assert hasattr(mod, "initialize_conflicts")
    assert mod.initialize_conflicts() == "conflicts initialized"
