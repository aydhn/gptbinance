def test_storage_init():
    import app.oversight_plane.storage as mod
    assert hasattr(mod, "initialize_storage")
    assert mod.initialize_storage() == "storage initialized"
