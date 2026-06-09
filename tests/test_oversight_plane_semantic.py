def test_semantic_init():
    import app.oversight_plane.semantic as mod
    assert hasattr(mod, "initialize_semantic")
    assert mod.initialize_semantic() == "semantic initialized"
