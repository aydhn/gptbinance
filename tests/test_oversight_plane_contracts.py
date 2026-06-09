def test_contracts_init():
    import app.oversight_plane.contracts as mod
    assert hasattr(mod, "initialize_contracts")
    assert mod.initialize_contracts() == "contracts initialized"
