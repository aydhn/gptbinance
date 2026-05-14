from typing import Dict, List
from app.supply_chain_plane.models import BuildInputRecord, ComponentRef


class BuildInputRegistry:
    def __init__(self):
        self._inputs: Dict[str, BuildInputRecord] = {}
        # Mapping from provenance_id to list of inputs
        self._provenance_inputs: Dict[str, List[str]] = {}

    def register_input(self, provenance_id: str, build_input: BuildInputRecord) -> None:
        self._inputs[build_input.input_id] = build_input
        if provenance_id not in self._provenance_inputs:
            self._provenance_inputs[provenance_id] = []
        self._provenance_inputs[provenance_id].append(build_input.input_id)

    def get_inputs_for_provenance(self, provenance_id: str) -> List[BuildInputRecord]:
        input_ids = self._provenance_inputs.get(provenance_id, [])
        return [self._inputs[i_id] for i_id in input_ids if i_id in self._inputs]
