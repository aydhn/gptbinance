import pytest
from app.provenance_plane.sources import get_authoritative_sources
from app.provenance_plane.registry import registry

def test_get_authoritative_sources():
    registry.register("source-1", {"provenance_id": "source-1", "class_type": "source", "source_authority": "authoritative"})
    sources = get_authoritative_sources()
    assert len(sources) >= 1
    assert sources[0]["provenance_id"] == "source-1"
