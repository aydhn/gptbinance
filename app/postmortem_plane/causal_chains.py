from typing import List
from app.postmortem_plane.models import CausalChain, CausalNode
from app.postmortem_plane.enums import CauseClass
from app.postmortem_plane.exceptions import InvalidCausalChainError

class CausalChainBuilder:
    @staticmethod
    def build_chain(chain_id: str, nodes: List[CausalNode], completeness: str, proof: str) -> CausalChain:
        has_symptom = any(n.cause_class == CauseClass.SYMPTOM for n in nodes)
        has_root = any(n.cause_class == CauseClass.ROOT_CAUSE for n in nodes)

        if not has_symptom:
             raise InvalidCausalChainError("Chain must have at least one symptom node")
        if not has_root:
             raise InvalidCausalChainError("Chain must have at least one root cause node")

        return CausalChain(
            chain_id=chain_id,
            nodes=nodes,
            completeness_notes=completeness,
            proof_notes=proof
        )
