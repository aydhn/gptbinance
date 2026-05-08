from app.execution_plane.enums import RoutingClass
from app.execution_plane.models import RoutingPolicy, ExecutionCandidate


class RoutingEngine:
    @staticmethod
    def evaluate(
        candidate: ExecutionCandidate, max_slippage_bps: float
    ) -> RoutingPolicy:
        # Default to passive for safety.
        routing_class = RoutingClass.PASSIVE
        rationale = "Default to passive execution for minimal slippage."
        urgency = "low"

        # In a more advanced implementation, urgency and slippage bounds
        # would be derived from the allocation intent's alpha decay profile.

        # For very large orders, we might prefer staged slices. This is just a stub.
        if candidate.target_size > 10.0:  # arbitrary threshold
            routing_class = RoutingClass.STAGED_SLICE
            rationale = "Large size detected, staged slice routing selected."
            urgency = "medium"

        return RoutingPolicy(
            routing_class=routing_class,
            urgency=urgency,
            rationale=rationale,
            max_slippage_bps=max_slippage_bps,
        )
