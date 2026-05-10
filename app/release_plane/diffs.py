from app.release_plane.models import ReleaseCandidate, ReleaseDefinition, ReleaseDiffRecord, ReleaseCandidateRef, ReleaseRef
import uuid

class ReleaseDiffEngine:
    def compare(self, candidate: ReleaseCandidate, active_release: ReleaseDefinition) -> ReleaseDiffRecord:
        summaries = []
        blast_radius = []

        # Example diff logic
        if candidate.definition.release_class != active_release.release_class:
             summaries.append(f"Class changed from {active_release.release_class} to {candidate.definition.release_class}")
             blast_radius.append("High: Release Class modified")

        if not summaries:
             summaries.append("No structural changes detected")
             blast_radius.append("None")

        return ReleaseDiffRecord(
            diff_id=f"diff-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate.candidate_id),
            active_release_ref=ReleaseRef(release_id=active_release.release_id),
            semantic_summaries=summaries,
            blast_radius_hints=blast_radius
        )
