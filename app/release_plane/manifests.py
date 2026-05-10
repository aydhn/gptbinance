from app.release_plane.models import ReleaseArtifactManifest, ReleaseCandidate, BundlePin
from app.release_plane.exceptions import ReleasePlaneError
import uuid

class ManifestBuilder:
    def build_manifest(self, candidate: ReleaseCandidate) -> ReleaseArtifactManifest:
        if not candidate.bundle:
            raise ReleasePlaneError("Cannot build manifest: missing bundle.")

        all_pins = []
        for entry in candidate.bundle.entries:
            all_pins.extend(entry.pins)

        return ReleaseArtifactManifest(
            manifest_id=f"manifest-{uuid.uuid4().hex[:8]}",
            candidate_ref={"candidate_id": candidate.candidate_id},
            bundle_hash=candidate.bundle.bundle_hash,
            pins=all_pins,
            lineage_refs=candidate.lineage_refs
        )
