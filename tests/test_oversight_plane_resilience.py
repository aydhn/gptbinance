def test_resilience_init():
    import app.oversight_plane.resilience as mod
    assert hasattr(mod, "initialize_resilience")
    assert mod.initialize_resilience() == "resilience initialized"
