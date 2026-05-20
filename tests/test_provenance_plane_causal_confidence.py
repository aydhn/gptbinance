import pytest
from app.provenance_plane.causal_confidence import get_causal_confidence
from app.provenance_plane.registry import registry

def test_get_causal_confidence():
    registry.register("outcome-3", {"provenance_id": "outcome-3", "causal_confidence": "HIGH"})
    assert get_causal_confidence("outcome-3") == "HIGH"
