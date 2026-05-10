import pytest
from app.postmortem_plane.causal_chains import CausalChainBuilder
from app.postmortem_plane.models import CausalNode
from app.postmortem_plane.enums import CauseClass
from app.postmortem_plane.exceptions import InvalidCausalChainError

def test_causal_chain_building():
    sym_node = CausalNode(node_id="N-1", cause_class=CauseClass.SYMPTOM, description="Timeout")
    root_node = CausalNode(node_id="N-2", cause_class=CauseClass.ROOT_CAUSE, description="Missing Index")

    chain = CausalChainBuilder.build_chain("C-1", [sym_node, root_node], "complete", "verified via logs")
    assert chain.chain_id == "C-1"

    with pytest.raises(InvalidCausalChainError):
        CausalChainBuilder.build_chain("C-2", [root_node], "complete", "no symptom")

    with pytest.raises(InvalidCausalChainError):
        CausalChainBuilder.build_chain("C-3", [sym_node], "complete", "no root")
