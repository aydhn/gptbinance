def test_manifests_init():
    import app.oversight_plane.manifests as mod
    assert hasattr(mod, "initialize_manifests")
    assert mod.initialize_manifests() == "manifests initialized"
