def test_meta_governance_init():
    import app.oversight_plane.meta_governance as mod
    assert hasattr(mod, "initialize_meta_governance")
    assert mod.initialize_meta_governance() == "meta_governance initialized"
