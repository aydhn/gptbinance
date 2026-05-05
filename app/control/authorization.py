from typing import Dict, Any, Optional
from datetime import datetime, timezone
from app.control.models import AuthorizationResult, ApprovalRecord
from app.control.enums import AuthorizationVerdict, ApprovalStatus


class AuthorizationEngine:
    def authorize(
        self, record: ApprovalRecord, execution_context: Optional[Dict[str, Any]] = None
    ) -> AuthorizationResult:
        now = datetime.now(timezone.utc)
        request = record.request

        # Check TTL
        if now > request.expires_at:
            return AuthorizationResult(
                request_id=request.id,
                verdict=AuthorizationVerdict.STALE,
                reason="Request has expired.",
                timestamp=now,
            )

        # Check Approval Status
        if record.status != ApprovalStatus.APPROVED:
            return AuthorizationResult(
                request_id=request.id,
                verdict=(
                    AuthorizationVerdict.REQUIRE_MORE_APPROVALS
                    if record.status == ApprovalStatus.PENDING
                    else AuthorizationVerdict.DENIED
                ),
                reason=f"Request status is {record.status.value}",
                timestamp=now,
            )

        # Re-evaluate context at execution time
        if execution_context:
            if (
                request.context.run_id
                and execution_context.get("run_id") != request.context.run_id
            ):
                return AuthorizationResult(
                    request_id=request.id,
                    verdict=AuthorizationVerdict.STALE,
                    reason="Context run_id mismatch at execution time.",
                    timestamp=now,
                )
            if (
                request.context.bundle_id
                and execution_context.get("bundle_id") != request.context.bundle_id
            ):
                return AuthorizationResult(
                    request_id=request.id,
                    verdict=AuthorizationVerdict.STALE,
                    reason="Context bundle_id mismatch at execution time.",
                    timestamp=now,
                )

        return AuthorizationResult(
            request_id=request.id,
            verdict=AuthorizationVerdict.APPROVED,
            reason="Authorized.",
            readiness_advisory=execution_context.get("readiness_advisory")
            if execution_context
            else None,
            timestamp=now,
        )


engine = AuthorizationEngine()


# Phase 43
def check_severe_shadow_drift_blockers(self):
    pass
