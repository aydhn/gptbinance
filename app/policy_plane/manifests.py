from app.policy_plane.models import PolicyArtifactManifest
import hashlib


def generate_manifest(policy_refs, eval_ids) -> PolicyArtifactManifest:
    m = hashlib.sha256()
    m.update(str(policy_refs).encode("utf-8"))
    return PolicyArtifactManifest(
        policy_refs=policy_refs,
        evaluation_ids=eval_ids,
        conflict_ids=[],
        exception_ids=[],
        debt_ids=[],
        hashes={"main": m.hexdigest()},
    )
