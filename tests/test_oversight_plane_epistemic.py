def test_epistemic_init():
    import app.oversight_plane.epistemic as mod
    assert hasattr(mod, "initialize_epistemic")
    assert mod.initialize_epistemic() == "epistemic initialized"
