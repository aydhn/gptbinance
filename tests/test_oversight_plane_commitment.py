def test_commitment_init():
    import app.oversight_plane.commitment as mod
    assert hasattr(mod, "initialize_commitment")
    assert mod.initialize_commitment() == "commitment initialized"
