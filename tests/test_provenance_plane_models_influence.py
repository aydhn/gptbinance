import pytest
from app.provenance_plane.models_influence import get_model_influence
from app.provenance_plane.registry import registry

def test_get_model_influence():
    registry.register("model-1", {"provenance_id": "model-1", "influence_strength": "STRONG"})
    assert get_model_influence("model-1") == "STRONG"
