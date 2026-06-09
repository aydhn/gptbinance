def test_stewardship_init():
    import app.oversight_plane.stewardship as mod
    assert hasattr(mod, "initialize_stewardship")
    assert mod.initialize_stewardship() == "stewardship initialized"
