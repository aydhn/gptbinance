from datetime import datetime, timezone
import hashlib
import json
from typing import List
from app.capacity_plane.models import (
    CapacityArtifactManifest,
    CapacityResourceRef,
    CapacityQuotaRef,
)
from app.capacity_plane.registry import capacity_registry
from app.capacity_plane.trust import evaluate_capacity_trust


def generate_capacity_manifest(manifest_id: str) -> CapacityArtifactManifest:
    resources = [
        CapacityResourceRef(resource_id=r.resource_id, class_name=r.class_name)
        for r in capacity_registry.list_resources()
    ]
    quotas = [
        CapacityQuotaRef(quota_id=q.quota_id, class_name=q.class_name)
        for q in capacity_registry.list_quotas()
    ]

    trust_verdict = evaluate_capacity_trust()

    # create deterministic hash
    content = {
        "resources": [r.model_dump() for r in resources],
        "quotas": [q.model_dump() for q in quotas],
        "verdict": trust_verdict.verdict.value,
    }
    manifest_hash = hashlib.sha256(
        json.dumps(content, sort_keys=True).encode()
    ).hexdigest()

    return CapacityArtifactManifest(
        manifest_id=manifest_id,
        resources=resources,
        quotas=quotas,
        verdict_ref=trust_verdict.verdict_id,
        timestamp=datetime.now(timezone.utc),
        hashes={"manifest_sha256": manifest_hash},
    )
