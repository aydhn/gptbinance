
def test_registry_integrity():
    from app.rights_plane.registry import CanonicalRightsRegistry
    registry = CanonicalRightsRegistry()
    registry.register_right("R-001", {"status": "active"})
    assert registry.get_right("R-001") == {"status": "active"}
