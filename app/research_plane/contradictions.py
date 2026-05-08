from app.research_plane.models import ContradictionRecord
from app.research_plane.exceptions import ContradictionHandlingError
from typing import List


class ContradictionTracker:
    def evaluate_burden(self, contradictions: List[ContradictionRecord]) -> dict:
        unresolved = [c for c in contradictions if c.unresolved_burden]
        resolved = [c for c in contradictions if not c.unresolved_burden]

        burden_level = "high" if len(unresolved) > 0 else "low"

        return {
            "unresolved_count": len(unresolved),
            "resolved_count": len(resolved),
            "burden_level": burden_level,
        }
