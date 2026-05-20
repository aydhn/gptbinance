import pytest
from app.provenance_plane.registry import CanonicalProvenanceRegistry
from app.provenance_plane.exceptions import InvalidProvenanceObject

def test_registry_registration():
    registry = CanonicalProvenanceRegistry()
    registry.register("prov-1", {"provenance_id": "prov-1", "data": "dummy"})
    assert registry.get("prov-1") is not None

def test_undocumented_provenance_rejection():
    registry = CanonicalProvenanceRegistry()
    with pytest.raises(InvalidProvenanceObject):
        registry.register("prov-2", {"data": "missing provenance_id"})
