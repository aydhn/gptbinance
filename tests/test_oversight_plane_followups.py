def test_followups_init():
    import app.oversight_plane.followups as mod
    assert hasattr(mod, "initialize_followups")
    assert mod.initialize_followups() == "followups initialized"
