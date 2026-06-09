def test_policy_init():
    import app.oversight_plane.policy as mod
    assert hasattr(mod, "initialize_policy")
    assert mod.initialize_policy() == "policy initialized"
