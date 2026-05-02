from datetime import datetime, timezone
from typing import List
from app.control.models import RevocationRecord, OperatorIdentity, ApprovalRecord
from app.control.enums import RevocationReason, ApprovalStatus


class RevocationManager:
    def __init__(self):
        self._records: List[RevocationRecord] = []

    def revoke(
        self,
        record: ApprovalRecord,
        operator: OperatorIdentity,
        reason: RevocationReason,
    ) -> RevocationRecord:
        now = datetime.now(timezone.utc)
        record.status = ApprovalStatus.REVOKED

        rev_record = RevocationRecord(
            request_id=record.request.id,
            revoked_by=operator,
            reason=reason,
            timestamp=now,
        )
        self._records.append(rev_record)
        return rev_record


manager = RevocationManager()
