from app.capacity_plane.manifests import generate_capacity_manifest
from app.capacity_plane.trust import evaluate_capacity_trust
from app.capacity_plane.storage import store_capacity_artifact


def save_latest_capacity_state():
    manifest = generate_capacity_manifest(manifest_id="latest")
    store_capacity_artifact("latest_manifest", manifest.model_dump())

    trust = evaluate_capacity_trust()
    store_capacity_artifact("latest_trust", trust.model_dump())


def get_latest_trust_verdict():
    from app.capacity_plane.storage import get_capacity_artifact

    return get_capacity_artifact("latest_trust")
