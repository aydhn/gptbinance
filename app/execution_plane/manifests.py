from app.execution_plane.models import (
    ExecutionArtifactManifest,
    ExecutionPlan,
    OrderSpecRef,
)
import hashlib


class ManifestBuilder:
    @staticmethod
    def build(plan: ExecutionPlan) -> ExecutionArtifactManifest:
        order_refs = []
        routing_refs = []
        for entry in plan.entries:
            order_refs.append(OrderSpecRef(spec_id=entry.order_spec.spec_id))
            routing_refs.append(entry.routing_policy.routing_class.value)

        # Simplified hash for immutability check
        hash_input = f"{plan.plan_id}_{len(order_refs)}"
        sig = hashlib.sha256(hash_input.encode()).hexdigest()

        return ExecutionArtifactManifest(
            plan_id=plan.plan_id,
            order_specs=order_refs,
            routing_refs=routing_refs,
            slice_refs=[],
            filter_refs=["filter_v1"],  # Stub
            idempotency_refs=[],  # Filled at send
            guard_refs=[],  # From plan entries
            hash_signature=sig,
            lineage_ref="manifest_builder_v1",
        )
