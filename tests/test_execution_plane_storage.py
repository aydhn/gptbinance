from app.execution_plane.storage import ExecutionStorage
from app.execution_plane.models import ExecutionArtifactManifest

def test_storage():
    s = ExecutionStorage()
    m = ExecutionArtifactManifest(plan_id="p", order_specs=[], routing_refs=[], slice_refs=[], filter_refs=[], idempotency_refs=[], guard_refs=[], hash_signature="a", lineage_ref="")
    s.save_manifest(m)

    m_out = s.get_manifest(m.manifest_id)
    assert m_out is not None
    assert m_out["hash_signature"] == "a"
