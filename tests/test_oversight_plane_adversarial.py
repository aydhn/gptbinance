def test_adversarial_init():
    import app.oversight_plane.adversarial as mod
    assert hasattr(mod, "initialize_adversarial")
    assert mod.initialize_adversarial() == "adversarial initialized"
