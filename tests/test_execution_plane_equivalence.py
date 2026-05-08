from app.execution_plane.equivalence import EquivalenceEngine
from app.execution_plane.models import ExecutionArtifactManifest
from app.execution_plane.enums import EquivalenceVerdictClass


def test_equivalence():
    m1 = ExecutionArtifactManifest(
        plan_id="p1",
        order_specs=[],
        routing_refs=[],
        slice_refs=[],
        filter_refs=[],
        idempotency_refs=[],
        guard_refs=[],
        hash_signature="aaa",
        lineage_ref="",
    )
    m2 = ExecutionArtifactManifest(
        plan_id="p2",
        order_specs=[],
        routing_refs=[],
        slice_refs=[],
        filter_refs=[],
        idempotency_refs=[],
        guard_refs=[],
        hash_signature="aaa",
        lineage_ref="",
    )
    m3 = ExecutionArtifactManifest(
        plan_id="p3",
        order_specs=[],
        routing_refs=[],
        slice_refs=[],
        filter_refs=[],
        idempotency_refs=[],
        guard_refs=[],
        hash_signature="bbb",
        lineage_ref="",
    )

    rep1 = EquivalenceEngine.compare(m1, m2)
    assert rep1.verdict == EquivalenceVerdictClass.CLEAN

    rep2 = EquivalenceEngine.compare(m1, m3)
    assert rep2.verdict == EquivalenceVerdictClass.DEGRADED
