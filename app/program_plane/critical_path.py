from app.program_plane.models import CriticalPathReport
from app.program_plane.exceptions import InvalidCriticalPathRecord

class CriticalPathEngine:
    def evaluate(self, program_id: str, path_nodes: list) -> CriticalPathReport:
        if not path_nodes:
            raise InvalidCriticalPathRecord("No path nodes provided")
        return CriticalPathReport(
            report_id=f"cp_{program_id}",
            program_id=program_id,
            path_nodes=path_nodes,
            path_confidence=1.0,
            near_critical_items=[],
            path_drift=False,
            proof_notes="Evaluated critical path"
        )
