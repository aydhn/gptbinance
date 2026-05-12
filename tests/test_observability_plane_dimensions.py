import pytest
from app.observability_plane.dimensions import DimensionRegistry
from app.observability_plane.models import DimensionDefinition
from app.observability_plane.exceptions import InvalidDimensionOrTagError

def test_dimension_scope_enforcement():
    reg = DimensionRegistry()
    with pytest.raises(InvalidDimensionOrTagError):
        reg.register_dimension(DimensionDefinition(dimension_id="dim1", scope="", is_mandatory=True))

    reg.register_dimension(DimensionDefinition(dimension_id="dim1", scope="env", is_mandatory=True))
    assert reg.get_dimension("dim1").scope == "env"
