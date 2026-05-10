from app.research_plane.models import EvidenceBundle, EvidenceBundleEntry
from app.research_plane.enums import EvidenceClass
from app.research_plane.exceptions import InvalidEvidenceBundleError


class EvidenceEvaluator:
    def evaluate_bundle(self, bundle: EvidenceBundle) -> dict:
        supportive_count = sum(
            1 for e in bundle.entries if e.evidence_class == EvidenceClass.SUPPORTIVE
        )
        contradictory_count = sum(
            1 for e in bundle.entries if e.evidence_class == EvidenceClass.CONTRADICTORY
        )

        if supportive_count > 0 and contradictory_count == 0:
            # We don't necessarily raise, but we flag it
            quality_note = (
                "Warning: One-sided evidence bundle. Missing contradiction surfaces."
            )
        else:
            quality_note = "Balanced evidence bundle."

        return {
            "supportive": supportive_count,
            "contradictory": contradictory_count,
            "quality_note": quality_note,
        }


class ResearchIntake:
    def intake_learning_note(self, learning_note: dict):
        pass
