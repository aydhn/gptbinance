import pytest
from app.provenance_plane.transformations import handle_transformation
from app.provenance_plane.registry import registry
from app.provenance_plane.exceptions import InvalidTransformation

def test_handle_transformation():
    registry.register("trans-1", {"provenance_id": "trans-1", "class_type": "transformation"})
    assert handle_transformation("trans-1") is True

def test_handle_invalid_transformation():
    registry.register("trans-invalid", {"provenance_id": "trans-invalid", "class_type": "input"})
    with pytest.raises(InvalidTransformation):
        handle_transformation("trans-invalid")
