from typing import Dict, Any
from app.learning_plane.models import LearningTrustVerdict, LearningObject
from app.learning_plane.enums import TrustVerdict, LessonClass, HardeningClass
from app.learning_plane.base import TrustEvaluatorBase
from app.learning_plane.storage import storage
from app.learning_plane.registry import CanonicalLearningRegistry

class TrustedLearningVerdictEngine(TrustEvaluatorBase):
    def __init__(self, registry: CanonicalLearningRegistry):
        self.registry = registry

    def evaluate_trust(self, learning_id: str) -> LearningTrustVerdict:
        obj = self.registry.get_object(learning_id)

        factors = {}
        caveats = []
        verdict = TrustVerdict.TRUSTED

        # Check Signal Coverage
        if not obj.signal_ids:
            factors["signal_coverage"] = "Poor"
            caveats.append("No signals attached to learning object.")
            verdict = TrustVerdict.DEGRADED
        else:
            factors["signal_coverage"] = "Adequate"

        # Check Findings Rigor
        if not obj.finding_ids:
            factors["finding_rigor"] = "Missing"
            caveats.append("No explicit findings documented.")
            if verdict == TrustVerdict.TRUSTED:
                verdict = TrustVerdict.CAUTION
        else:
             factors["finding_rigor"] = "Present"

        # Check Causal Honesty
        if not obj.cause_ids and obj.hypothesis_ids:
             factors["causal_honesty"] = "Unvalidated Hypotheses"
             caveats.append("Hypotheses exist but lack validated causes.")
             verdict = TrustVerdict.REVIEW_REQUIRED
        elif not obj.cause_ids:
             factors["causal_honesty"] = "Missing"
             caveats.append("No validated causes attached.")
             if verdict in [TrustVerdict.TRUSTED, TrustVerdict.CAUTION]:
                verdict = TrustVerdict.DEGRADED
        else:
             factors["causal_honesty"] = "Validated"

        # Check Lesson Clarity
        if not obj.lesson_ids:
            factors["lesson_clarity"] = "Missing"
            caveats.append("No extracted lessons.")
            verdict = TrustVerdict.BLOCKED
        else:
            factors["lesson_clarity"] = "Present"

        # Check Update-Target completeness & Validation Posture
        if not obj.target_ids:
             factors["update_targets"] = "Orphaned Lessons"
             caveats.append("Lessons exist without update targets.")
             verdict = TrustVerdict.BLOCKED
        else:
             factors["update_targets"] = "Complete"

        if not obj.validation_ids and obj.action_ids:
             factors["validation_posture"] = "Unvalidated Hardening"
             caveats.append("Hardening actions exist but lack anti-recurrence validation.")
             verdict = TrustVerdict.CAUTION
        elif not obj.validation_ids:
             factors["validation_posture"] = "Missing"
             caveats.append("No validation records present.")
        else:
             factors["validation_posture"] = "Validated"

        # Recurrence check
        if obj.recurrence_ids:
            factors["recurrence_control"] = "Failed"
            caveats.append("Recurrence detected for this learning class.")
            verdict = TrustVerdict.BLOCKED
        else:
            factors["recurrence_control"] = "Effective"

        storage.save_trust_verdict(learning_id, LearningTrustVerdict(verdict=verdict, factors=factors, caveats=caveats))
        return storage.get_trust_verdict(learning_id)
