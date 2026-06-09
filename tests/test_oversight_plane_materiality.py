def test_materiality_init():
    import app.oversight_plane.materiality as mod
    assert hasattr(mod, "initialize_materiality")
    assert mod.initialize_materiality() == "materiality initialized"
