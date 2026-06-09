def test_spot_audits_init():
    import app.oversight_plane.spot_audits as mod
    assert hasattr(mod, "initialize_spot_audits")
    assert mod.initialize_spot_audits() == "spot_audits initialized"
