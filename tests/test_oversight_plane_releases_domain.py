def test_releases_domain_init():
    import app.oversight_plane.releases_domain as mod
    assert hasattr(mod, "initialize_releases_domain")
    assert mod.initialize_releases_domain() == "releases_domain initialized"
