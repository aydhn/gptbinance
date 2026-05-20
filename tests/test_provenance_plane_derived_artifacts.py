import pytest
from app.provenance_plane.derived_artifacts import get_derived_artifact
from app.provenance_plane.registry import registry

def test_get_derived_artifact():
    registry.register("artifact-1", {"provenance_id": "artifact-1", "class_type": "derived_artifact"})
    artifact = get_derived_artifact("artifact-1")
    assert artifact["provenance_id"] == "artifact-1"
