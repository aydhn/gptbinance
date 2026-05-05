from typing import List
from app.readiness_board.models import EvidenceConflict


class ContradictionResolver:
    def resolve(self, conflicts: List[EvidenceConflict]) -> List[EvidenceConflict]:
        resolved = []
        for c in conflicts:
            # We don't automatically resolve things.
            # This is where safety-critical precedence could auto-resolve some by deferring to policy.
            # For now, return as unresolved unless explicitly handled.
            resolved.append(c)
        return resolved
