def test_assurance_init():
    import app.oversight_plane.assurance as mod
    assert hasattr(mod, "initialize_assurance")
    assert mod.initialize_assurance() == "assurance initialized"
