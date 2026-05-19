from typing import List, Dict, Optional
from app.learning_plane.models import LearningEquivalenceReport, LearningDivergenceReport, LearningObject
from app.learning_plane.enums import EquivalenceVerdict
from app.learning_plane.storage import storage

class EquivalenceAnalyzer:
    def compare_environments(self, base_learning_id: str, compare_learning_id: str) -> LearningEquivalenceReport:
        base_obj = storage.get_object(base_learning_id)
        compare_obj = storage.get_object(compare_learning_id)

        if not base_obj or not compare_obj:
            return LearningEquivalenceReport(
                report_id=f"equiv_{base_learning_id}_{compare_learning_id}",
                verdict=EquivalenceVerdict.UNKNOWN,
                blockers=["Missing learning object(s) for comparison."],
                proof_notes="Cannot perform equivalence check."
            )

        blockers = []

        if set(base_obj.signal_ids) != set(compare_obj.signal_ids):
             blockers.append("Signal mismatch between environments.")

        if set(base_obj.lesson_ids) != set(compare_obj.lesson_ids):
             blockers.append("Lesson extraction divergence detected.")

        if set(base_obj.action_ids) != set(compare_obj.action_ids):
             blockers.append("Hardening actions differ across environments.")

        verdict = EquivalenceVerdict.EQUIVALENT
        if blockers:
            verdict = EquivalenceVerdict.DIVERGENT
            self.create_divergence_report(base_learning_id, compare_learning_id, blockers)

        report = LearningEquivalenceReport(
            report_id=f"equiv_{base_learning_id}_{compare_learning_id}",
            verdict=verdict,
            blockers=blockers,
            proof_notes=f"Comparison between {base_learning_id} and {compare_learning_id} complete."
        )
        storage.save_equivalence_report(report)
        return report

    def create_divergence_report(self, base_id: str, compare_id: str, blockers: List[str]):
         report = LearningDivergenceReport(
             report_id=f"div_{base_id}_{compare_id}",
             divergence_type="environment_learning_divergence",
             severity="high",
             description=f"Divergence detected: {', '.join(blockers)}"
         )
         storage.save_divergence_report(report)
