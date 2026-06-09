def test_debt_init():
    import app.oversight_plane.debt as mod
    assert hasattr(mod, "initialize_debt")
    assert mod.initialize_debt() == "debt initialized"
