from datetime import datetime, timezone
from app.control.models import ApprovalRecord
from app.control.enums import ApprovalStatus


class ExpiryManager:
    def check_and_expire(self, record: ApprovalRecord) -> bool:
        if record.status not in (ApprovalStatus.PENDING, ApprovalStatus.APPROVED):
            return False

        now = datetime.now(timezone.utc)
        if now > record.request.expires_at:
            record.status = ApprovalStatus.EXPIRED
            return True
        return False


manager = ExpiryManager()
