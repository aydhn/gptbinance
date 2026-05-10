from typing import List
from app.postmortem_plane.models import RootCauseRecord

class RootCauseDiscipline:
    @staticmethod
    def create_root_cause(rc_id: str, desc: str, node_refs: List[str], threshold_met: bool, notes: str) -> RootCauseRecord:
        return RootCauseRecord(
            root_cause_id=rc_id,
            description=desc,
            causal_node_refs=node_refs,
            is_multi_root=len(node_refs) > 1,
            evidence_threshold_met=threshold_met,
            proof_notes=notes
        )
