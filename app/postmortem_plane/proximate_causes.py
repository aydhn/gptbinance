from typing import List
from app.postmortem_plane.models import ProximateCauseRecord

class ProximateCauseHandler:
    @staticmethod
    def create_proximate_cause(pc_id: str, desc: str, node_refs: List[str], lineages: List[str]) -> ProximateCauseRecord:
        return ProximateCauseRecord(
            proximate_cause_id=pc_id,
            description=desc,
            causal_node_refs=node_refs,
            lineage_refs=lineages
        )
