def test_inspections_init():
    import app.oversight_plane.inspections as mod
    assert hasattr(mod, "initialize_inspections")
    assert mod.initialize_inspections() == "inspections initialized"
