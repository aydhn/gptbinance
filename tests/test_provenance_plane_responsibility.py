import pytest
from app.provenance_plane.responsibility import get_responsibility
from app.provenance_plane.registry import registry

def test_get_responsibility():
    registry.register("obj-1", {"provenance_id": "obj-1", "accountable_actors": ["user1"]})
    assert len(get_responsibility("obj-1")) == 1
