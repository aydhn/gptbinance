import pytest
from app.provenance_plane.attribution import get_attribution
from app.provenance_plane.registry import registry
from app.provenance_plane.exceptions import InvalidAttribution

def test_valid_attribution():
    registry.register("attr-obj-1", {"provenance_id": "attr-obj-1", "attribution": {"actor": "agent-x"}})
    attribution = get_attribution("attr-obj-1")
    assert attribution["actor"] == "agent-x"

def test_invalid_attribution():
    registry.register("attr-obj-2", {"provenance_id": "attr-obj-2"})
    with pytest.raises(InvalidAttribution):
        get_attribution("attr-obj-2")
