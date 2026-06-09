def test_escalation_init():
    import app.oversight_plane.escalation as mod
    assert hasattr(mod, "initialize_escalation")
    assert mod.initialize_escalation() == "escalation initialized"
