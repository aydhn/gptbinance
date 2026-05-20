import pytest
from app.provenance_plane.features import get_feature_lineage
from app.provenance_plane.registry import registry

def test_get_feature_lineage():
    registry.register("feature-1", {"provenance_id": "feature-1", "lineage_refs": [{"provenance_id": "artifact-1", "ref_type": "artifact"}]})
    assert len(get_feature_lineage("feature-1")) == 1
