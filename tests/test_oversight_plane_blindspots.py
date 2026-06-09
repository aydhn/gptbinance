def test_blindspots_init():
    import app.oversight_plane.blindspots as mod
    assert hasattr(mod, "initialize_blindspots")
    assert mod.initialize_blindspots() == "blindspots initialized"
