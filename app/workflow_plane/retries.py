from app.workflow_plane.models import RetryRecord
from app.workflow_plane.enums import RetryClass
from app.workflow_plane.exceptions import InvalidRetryError
import uuid

class RetryManager:
    def __init__(self):
        self.records = []

    def register_retry(self, run_id: str, reason: str, retry_count: int, retry_class: RetryClass) -> RetryRecord:
        if retry_class == RetryClass.NON_RETRYABLE:
            raise InvalidRetryError("Attempted to retry a non-retryable run")

        record = RetryRecord(
            retry_id=f"ret-{uuid.uuid4().hex[:8]}",
            run_id=run_id,
            reason=reason,
            retry_class=retry_class,
            retry_count=retry_count
        )
        self.records.append(record)
        return record
