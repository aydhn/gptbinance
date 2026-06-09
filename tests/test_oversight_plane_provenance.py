def test_provenance_init():
    import app.oversight_plane.provenance as mod
    assert hasattr(mod, "initialize_provenance")
    assert mod.initialize_provenance() == "provenance initialized"
