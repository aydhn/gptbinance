def test_migrations_init():
    import app.oversight_plane.migrations as mod
    assert hasattr(mod, "initialize_migrations")
    assert mod.initialize_migrations() == "migrations initialized"
