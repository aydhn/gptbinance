def test_constitution_init():
    import app.oversight_plane.constitution as mod
    assert hasattr(mod, "initialize_constitution")
    assert mod.initialize_constitution() == "constitution initialized"
