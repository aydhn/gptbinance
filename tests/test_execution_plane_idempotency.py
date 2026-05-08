import pytest
from app.execution_plane.idempotency import IdempotencyStore
from app.execution_plane.exceptions import IdempotencyViolationError

def test_idempotency_store():
    store = IdempotencyStore()
    record = store.register("key1", "intent1")
    assert record.idempotency_key == "key1"

    with pytest.raises(IdempotencyViolationError):
        store.register("key1", "intent2")

    store.mark_stale("key1")
    store.register("key1", "intent3") # should be ok now
