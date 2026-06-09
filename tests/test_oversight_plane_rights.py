def test_rights_init():
    import app.oversight_plane.rights as mod
    assert hasattr(mod, "initialize_rights")
    assert mod.initialize_rights() == "rights initialized"
