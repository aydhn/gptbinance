import pytest
from app.provenance_plane.decisions import check_decision_lineage
from app.provenance_plane.registry import registry

def test_check_decision_lineage():
    registry.register("decision-1", {"provenance_id": "decision-1", "lineage_refs": [{"provenance_id": "config-1"}]})
    assert check_decision_lineage("decision-1") is True
