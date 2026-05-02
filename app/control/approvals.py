from typing import Dict, Optional
from datetime import datetime, timezone
from app.control.models import (
    ActionRequest,
    ApprovalRecord,
    ApprovalDecision,
    OperatorIdentity,
)
from app.control.enums import ApprovalStatus
from app.control.exceptions import InvalidActionRequest
from app.control.policies import engine as policy_engine


class ApprovalManager:
    def __init__(self):
        self._records: Dict[str, ApprovalRecord] = {}

    def init_record(self, request: ActionRequest) -> ApprovalRecord:
        record = ApprovalRecord(request=request)
        self._records[request.id] = record
        return record

    def get_record(self, request_id: str) -> Optional[ApprovalRecord]:
        return self._records.get(request_id)

    def add_decision(
        self,
        request_id: str,
        approver: OperatorIdentity,
        approved: bool,
        reason: str = "",
    ) -> ApprovalRecord:
        record = self.get_record(request_id)
        if not record:
            raise InvalidActionRequest(f"Request {request_id} not found.")

        if record.status not in (ApprovalStatus.PENDING,):
            raise InvalidActionRequest(
                f"Cannot add decision to request in status {record.status}"
            )

        now = datetime.now(timezone.utc)
        decision = ApprovalDecision(
            request_id=request_id,
            approver=approver,
            approved=approved,
            reason=reason,
            timestamp=now,
        )
        record.decisions.append(decision)

        # Check if rejected
        if not approved:
            record.status = ApprovalStatus.REJECTED
            return record

        # Evaluate policies
        if policy_engine.evaluate(record.request, record):
            record.status = ApprovalStatus.APPROVED

        return record


manager = ApprovalManager()
