def test_evidence_init():
    import app.oversight_plane.evidence as mod
    assert hasattr(mod, "initialize_evidence")
    assert mod.initialize_evidence() == "evidence initialized"
