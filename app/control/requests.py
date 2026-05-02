import uuid
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional
from app.control.models import (
    ActionRequest,
    ActionRequestContext,
    OperatorIdentity,
)
from app.control.enums import SensitiveActionType
from app.control.actions import registry as action_registry
from app.control.exceptions import InvalidActionRequest


class RequestManager:
    def create_request(
        self,
        action_type: SensitiveActionType,
        requester: OperatorIdentity,
        rationale: str,
        context_data: Optional[Dict[str, Any]] = None,
        run_id: Optional[str] = None,
        bundle_id: Optional[str] = None,
    ) -> ActionRequest:
        action = action_registry.get_action(action_type)
        if not action:
            raise InvalidActionRequest(f"Unknown action type: {action_type}")

        if not rationale:
            raise InvalidActionRequest("Rationale is required for sensitive actions.")

        ttl = action.ttl_seconds
        now = datetime.now(timezone.utc)
        expires_at = now + timedelta(seconds=ttl)

        ctx = ActionRequestContext(
            run_id=run_id, bundle_id=bundle_id, additional_metadata=context_data or {}
        )

        req_id = f"req-{uuid.uuid4().hex[:8]}"

        return ActionRequest(
            id=req_id,
            action_type=action_type,
            requester=requester,
            context=ctx,
            rationale=rationale,
            created_at=now,
            expires_at=expires_at,
        )


manager = RequestManager()
