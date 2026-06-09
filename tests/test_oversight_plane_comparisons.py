def test_comparisons_init():
    import app.oversight_plane.comparisons as mod
    assert hasattr(mod, "initialize_comparisons")
    assert mod.initialize_comparisons() == "comparisons initialized"
