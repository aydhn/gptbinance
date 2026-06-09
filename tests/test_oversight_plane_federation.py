def test_federation_init():
    import app.oversight_plane.federation as mod
    assert hasattr(mod, "initialize_federation")
    assert mod.initialize_federation() == "federation initialized"
