import pytest
from app.provenance_plane.inputs import get_input_lineage
from app.provenance_plane.registry import registry

def test_get_input_lineage():
    registry.register("input-1", {"provenance_id": "input-1", "lineage_refs": [{"provenance_id": "source-1", "ref_type": "source"}]})
    lineage = get_input_lineage("input-1")
    assert len(lineage) == 1
    assert lineage[0]["provenance_id"] == "source-1"
