import pytest
from app.provenance_plane.custody import get_custody_chain
from app.provenance_plane.registry import registry

def test_custody_chain_retrieval():
    registry.register("custody-obj-1", {"provenance_id": "custody-obj-1", "custody_chain": [{"step": "transform", "status": "VERIFIED"}]})
    chain = get_custody_chain("custody-obj-1")
    assert len(chain) == 1
    assert chain[0]["step"] == "transform"
