from typing import List, Optional
from app.control.models import ApprovalRecord
from app.control.enums import ApprovalStatus
from app.control.storage import storage
from app.control.approvals import manager as approval_manager


class ControlRepository:
    def save(self, record: ApprovalRecord) -> None:
        storage.save_record(record)
        # In-memory sync for now
        approval_manager._records[record.request.id] = record

    def get(self, request_id: str) -> Optional[ApprovalRecord]:
        return approval_manager.get_record(request_id)

    def get_pending(self) -> List[ApprovalRecord]:
        return [
            r
            for r in approval_manager._records.values()
            if r.status == ApprovalStatus.PENDING
        ]


repository = ControlRepository()
