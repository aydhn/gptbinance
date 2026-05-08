from app.execution_plane.models import CancelReplaceChain
from app.execution_plane.exceptions import CancelReplaceViolationError
from typing import Dict


class CancelReplaceManager:
    def __init__(self):
        self._chains: Dict[str, CancelReplaceChain] = {}

    def initiate_chain(self, original_spec_id: str) -> CancelReplaceChain:
        chain = CancelReplaceChain(
            original_spec_id=original_spec_id, lineage_ref="crm_v1"
        )
        self._chains[original_spec_id] = chain
        return chain

    def add_replacement(self, original_spec_id: str, new_spec_id: str):
        if original_spec_id not in self._chains:
            raise CancelReplaceViolationError(
                f"No active chain for original spec: {original_spec_id}"
            )

        chain = self._chains[original_spec_id]
        if chain.is_ambiguous:
            raise CancelReplaceViolationError("Cannot replace an ambiguous chain.")

        chain.replaced_spec_ids.append(new_spec_id)

    def mark_ambiguous(self, original_spec_id: str, reason: str):
        if original_spec_id in self._chains:
            self._chains[original_spec_id].is_ambiguous = True
            self._chains[original_spec_id].stale_reason = reason
