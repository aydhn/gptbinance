from app.execution_plane.models import (
    ExecutionPlan,
    ExecutionPlanEntry,
    OrderSpec,
    RoutingPolicy,
    ExecutionCandidate,
)
from typing import List


class ExecutionPlanBuilder:
    @staticmethod
    def build(
        source_allocation_id: str,
        candidate: ExecutionCandidate,
        order_spec: OrderSpec,
        routing: RoutingPolicy,
        guards: List[str],
    ) -> ExecutionPlan:
        entry = ExecutionPlanEntry(
            candidate_id=candidate.candidate_id,
            order_spec=order_spec,
            routing_policy=routing,
            guard_refs=guards,
        )

        return ExecutionPlan(
            source_allocation_intent_id=source_allocation_id,
            entries=[entry],
            venue_scope=[order_spec.venue_id],
        )
