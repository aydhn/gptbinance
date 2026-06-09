def test_equivalence_init():
    import app.oversight_plane.equivalence as mod
    assert hasattr(mod, "initialize_equivalence")
    assert mod.initialize_equivalence() == "equivalence initialized"
