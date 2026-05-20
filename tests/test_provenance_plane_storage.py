import pytest
from app.provenance_plane.storage import store_provenance_object
from app.provenance_plane.registry import registry

def test_store_provenance_object():
    store_provenance_object("obj-store-1", {"provenance_id": "obj-store-1"})
    assert registry.get("obj-store-1") is not None
