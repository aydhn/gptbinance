from app.execution_plane.models import IdempotencyRecord
from app.execution_plane.exceptions import IdempotencyViolationError
from typing import Dict

class IdempotencyStore:
    def __init__(self):
        self._records: Dict[str, IdempotencyRecord] = {}

    def get_record(self, key: str) -> IdempotencyRecord | None:
        return self._records.get(key)

    def register(self, key: str, intent_ref: str, retry_window_ms: int = 60000) -> IdempotencyRecord:
        if key in self._records:
            if not self._records[key].is_stale:
                raise IdempotencyViolationError(f"Active idempotency key already exists: {key}")

        record = IdempotencyRecord(
            idempotency_key=key,
            intent_ref=intent_ref,
            retry_window_ms=retry_window_ms,
            audit_ref="local_idempotency_store"
        )
        self._records[key] = record
        return record

    def mark_stale(self, key: str):
        if key in self._records:
            self._records[key].is_stale = True
