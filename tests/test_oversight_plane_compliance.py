def test_compliance_init():
    import app.oversight_plane.compliance as mod
    assert hasattr(mod, "initialize_compliance")
    assert mod.initialize_compliance() == "compliance initialized"
