import pytest
from app.provenance_plane.comparisons import compare_provenance
from app.provenance_plane.registry import registry

def test_compare_provenance():
    registry.register("obj-1", {"provenance_id": "obj-1", "lineage_refs": ["ref1"]})
    registry.register("obj-2", {"provenance_id": "obj-2", "lineage_refs": ["ref1"]})
    assert compare_provenance("obj-1", "obj-2") is True
