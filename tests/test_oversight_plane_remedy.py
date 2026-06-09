def test_remedy_init():
    import app.oversight_plane.remedy as mod
    assert hasattr(mod, "initialize_remedy")
    assert mod.initialize_remedy() == "remedy initialized"
