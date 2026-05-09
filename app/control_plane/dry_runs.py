from app.control_plane.models import ActionRequest, ActionDryRunResult
from app.control_plane.enums import PreviewClass


class DryRunEngine:
    def run_dry(self, request: ActionRequest) -> ActionDryRunResult:
        return ActionDryRunResult(
            action_id=request.action_id,
            fidelity_class=PreviewClass.FULL_FIDELITY,
            hypothetical_receipts=["mock-receipt-1"],
            simulated_outcomes={"state_change": "SUCCESS"},
        )
