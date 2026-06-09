def test_scenario_init():
    import app.oversight_plane.scenario as mod
    assert hasattr(mod, "initialize_scenario")
    assert mod.initialize_scenario() == "scenario initialized"
