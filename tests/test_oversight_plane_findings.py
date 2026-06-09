def test_findings_init():
    import app.oversight_plane.findings as mod
    assert hasattr(mod, "initialize_findings")
    assert mod.initialize_findings() == "findings initialized"
