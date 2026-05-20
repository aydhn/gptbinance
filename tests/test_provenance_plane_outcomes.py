import pytest
from app.provenance_plane.outcomes import get_outcome_lineage
from app.provenance_plane.registry import registry

def test_get_outcome_lineage():
    registry.register("outcome-1", {"provenance_id": "outcome-1", "lineage_refs": [{"provenance_id": "action-1"}]})
    assert len(get_outcome_lineage("outcome-1")) == 1
