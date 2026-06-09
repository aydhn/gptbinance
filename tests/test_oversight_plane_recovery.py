def test_recovery_init():
    import app.oversight_plane.recovery as mod
    assert hasattr(mod, "initialize_recovery")
    assert mod.initialize_recovery() == "recovery initialized"
