import pytest
from app.provenance_plane.contributions import get_contributions
from app.provenance_plane.registry import registry

def test_get_contributions():
    registry.register("outcome-2", {"provenance_id": "outcome-2", "contributing_factors": ["factor1"]})
    assert len(get_contributions("outcome-2")) == 1
