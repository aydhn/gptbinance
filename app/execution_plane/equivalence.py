from app.execution_plane.models import ExecutionEquivalenceReport, ExecutionArtifactManifest
from app.execution_plane.enums import EquivalenceVerdictClass

class EquivalenceEngine:
    @staticmethod
    def compare(runtime_manifest: ExecutionArtifactManifest, replay_manifest: ExecutionArtifactManifest) -> ExecutionEquivalenceReport:
        blockers = []
        verdict = EquivalenceVerdictClass.CLEAN

        if runtime_manifest.hash_signature != replay_manifest.hash_signature:
             blockers.append("hash_mismatch")
             verdict = EquivalenceVerdictClass.DEGRADED

        if len(runtime_manifest.order_specs) != len(replay_manifest.order_specs):
             blockers.append("order_count_mismatch")
             verdict = EquivalenceVerdictClass.BLOCKED

        return ExecutionEquivalenceReport(
            runtime_manifest_id=runtime_manifest.manifest_id,
            replay_manifest_id=replay_manifest.manifest_id,
            verdict=verdict,
            blockers=blockers,
            proof_notes="Compared hash and order count."
        )
