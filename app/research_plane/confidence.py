from app.research_plane.models import (
    ConfidenceAssessment,
    EvidenceBundle,
    ContradictionRecord,
)
from app.research_plane.enums import ConfidenceClass
from app.research_plane.exceptions import ConfidenceViolationError
from typing import List


class ConfidenceLadderManager:
    def evaluate_transition(
        self,
        current_class: ConfidenceClass,
        target_class: ConfidenceClass,
        evidence: EvidenceBundle,
        contradictions: List[ContradictionRecord],
    ) -> bool:
        # Prevent unjustified jumps. Example: Cannot jump from SPECULATIVE to EXPERIMENT_READY directly
        ladder = [
            ConfidenceClass.SPECULATIVE,
            ConfidenceClass.PLAUSIBLE,
            ConfidenceClass.EVIDENCE_SUPPORTED,
            ConfidenceClass.EXPERIMENT_READY,
            ConfidenceClass.STRATEGY_CANDIDATE,
        ]

        if target_class in ladder and current_class in ladder:
            current_idx = ladder.index(current_class)
            target_idx = ladder.index(target_class)

            if target_idx > current_idx + 1:
                raise ConfidenceViolationError(
                    f"Unjustified confidence jump from {current_class.name} to {target_class.name}"
                )

            if target_class == ConfidenceClass.EVIDENCE_SUPPORTED:
                if not evidence.entries:
                    raise ConfidenceViolationError(
                        "Cannot move to EVIDENCE_SUPPORTED without evidence."
                    )

            if target_class == ConfidenceClass.EXPERIMENT_READY:
                unresolved = [c for c in contradictions if c.unresolved_burden]
                if unresolved:
                    raise ConfidenceViolationError(
                        "Cannot move to EXPERIMENT_READY with unresolved contradictions."
                    )

        return True
