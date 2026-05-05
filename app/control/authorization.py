from datetime import datetime, timezone
from app.control.models import AuthorizationResult, ApprovalRecord, ActionRequest
from app.control.enums import AuthorizationVerdict
from app.policy_kernel.evaluation import evaluate_policy
from app.policy_kernel.context import assemble_policy_context
from app.policy_kernel.evidence import assemble_evidence_bundle
from app.policy_kernel.enums import PolicyVerdict


class ControlAuthorization:
    def check_remediation_apply_scope(self):
        pass

    def check_policy_constitution(
        self,
        action_type: str,
        workspace_id: str,
        profile_id: str,
        mode: str,
        evidence_kwargs: dict = None,
    ) -> bool:
        if evidence_kwargs is None:
            evidence_kwargs = {}

        ctx = assemble_policy_context(action_type, workspace_id, profile_id, mode)
        ev_bundle = assemble_evidence_bundle(**evidence_kwargs)

        decision = evaluate_policy(action_type, ctx, ev_bundle)

        if decision.final_verdict == PolicyVerdict.HARD_BLOCK:
            print(
                f"Policy Kernel DENIED action {action_type} due to HARD_BLOCK. Reason: {decision.reasoning}"
            )
            return False

        return True

    def authorize(self, record: ApprovalRecord) -> AuthorizationResult:
        # Pre-check policy constitution before finalizing authorization
        action_type = record.request.action_type.value
        workspace_id = record.request.context.additional_metadata.get(
            "workspace_id", "default"
        )
        profile_id = record.request.context.additional_metadata.get(
            "profile_id", "default"
        )
        mode = record.request.context.additional_metadata.get("mode", "paper")

        policy_ok = self.check_policy_constitution(
            action_type, workspace_id, profile_id, mode
        )

        if not policy_ok:
            return AuthorizationResult(
                request_id=record.request.id,
                verdict=AuthorizationVerdict.DENIED,
                reason="Denied by Policy Constitution (HARD_BLOCK).",
                timestamp=datetime.now(timezone.utc),
            )

        # Simplified normal authorization logic
        from app.control.enums import ApprovalStatus

        if record.status == ApprovalStatus.APPROVED:
            return AuthorizationResult(
                request_id=record.request.id,
                verdict=AuthorizationVerdict.APPROVED,
                reason="Approved by control engine and policy constitution.",
                timestamp=datetime.now(timezone.utc),
            )
        else:
            return AuthorizationResult(
                request_id=record.request.id,
                verdict=AuthorizationVerdict.DENIED,
                reason="Denied by control engine.",
                timestamp=datetime.now(timezone.utc),
            )
