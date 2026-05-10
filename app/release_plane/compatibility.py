from app.release_plane.models import ReleaseCandidate, CompatibilityReport, EnvironmentTarget, ReleaseCandidateRef
from app.release_plane.enums import EnvironmentClass
from app.release_plane.base import CompatibilityEvaluatorBase
import uuid

class StandardCompatibilityEvaluator(CompatibilityEvaluatorBase):
    def evaluate(self, candidate: ReleaseCandidate, target_env: EnvironmentTarget) -> CompatibilityReport:
        is_compatible = True
        missing_deps = []
        blockers = []

        # Example check: ensure all bundle entries have required pins
        for entry in candidate.bundle.entries:
            if not entry.pins:
                is_compatible = False
                blockers.append(f"Missing dependency blockers: Entry {entry.entry_id} has no pins.")

        # Check environment fit
        if target_env.environment_class not in [t.environment_class for t in candidate.definition.target_environments]:
             is_compatible = False
             blockers.append(f"Environment {target_env.environment_class} is not in target environments.")

        return CompatibilityReport(
            report_id=f"cr-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate.candidate_id),
            environment=target_env.environment_class,
            is_compatible=is_compatible,
            missing_dependencies=missing_deps,
            blockers=blockers,
            proof_notes="Compatibility evaluated successfully."
        )
