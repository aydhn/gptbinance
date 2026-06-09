def test_objects_init():
    import app.oversight_plane.objects as mod
    assert hasattr(mod, "initialize_objects")
    assert mod.initialize_objects() == "objects initialized"
