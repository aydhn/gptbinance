import pytest
from app.policy_plane.manifests import generate_manifest
from app.policy_plane.models import PolicyRef


def test_generate_manifest():
    refs = [PolicyRef(policy_id="POL-1", version="1.0.0")]
    eval_ids = ["eval-1", "eval-2"]

    manifest = generate_manifest(refs, eval_ids)
    assert manifest is not None
    assert len(manifest.policy_refs) == 1
    assert len(manifest.evaluation_ids) == 2
    assert "main" in manifest.hashes
