import pytest
from app.observability_plane.tags import TagRegistry
from app.observability_plane.models import TagDefinition
from app.observability_plane.exceptions import InvalidDimensionOrTagError

def test_tag_cardinality_enforcement():
    reg = TagRegistry()
    with pytest.raises(InvalidDimensionOrTagError):
        reg.register_tag(TagDefinition(tag_id="tag1", cardinality_expectation=""))

    reg.register_tag(TagDefinition(tag_id="tag1", cardinality_expectation="low"))
    assert reg.get_tag("tag1").cardinality_expectation == "low"
