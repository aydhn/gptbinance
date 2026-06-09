def test_jurisdiction_init():
    import app.oversight_plane.jurisdiction as mod
    assert hasattr(mod, "initialize_jurisdiction")
    assert mod.initialize_jurisdiction() == "jurisdiction initialized"
