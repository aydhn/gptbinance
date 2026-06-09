def test_orchestration_init():
    import app.oversight_plane.orchestration as mod
    assert hasattr(mod, "initialize_orchestration")
    assert mod.initialize_orchestration() == "orchestration initialized"
