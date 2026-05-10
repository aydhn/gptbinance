import hashlib
import json
from app.postmortem_plane.models import PostmortemArtifactManifest, PostmortemDefinition

class PostmortemManifestBuilder:
    @staticmethod
    def build(manifest_id: str, postmortem: PostmortemDefinition) -> PostmortemArtifactManifest:
        # Simple hash of the id for demo
        h = hashlib.sha256(postmortem.postmortem_id.encode()).hexdigest()
        return PostmortemArtifactManifest(
            manifest_id=manifest_id,
            postmortem_id=postmortem.postmortem_id,
            incident_refs=postmortem.source_incidents.incident_ids if postmortem.source_incidents else [],
            evidence_refs=[e.evidence_id for e in postmortem.evidence_reviews],
            cause_refs=[c.root_cause_id for c in postmortem.root_causes],
            contributor_refs=[c.contributor_id for c in postmortem.contributors],
            action_refs=[a.action_id for a in postmortem.corrective_actions + postmortem.preventive_actions],
            verification_refs=[],
            debt_refs=[d.debt_id for d in postmortem.debt_records],
            closure_refs=[],
            hashes={"definition": h}
        )
