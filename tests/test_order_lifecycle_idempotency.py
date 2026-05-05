from app.order_lifecycle.idempotency import IdempotencyEngine
from app.order_lifecycle.exceptions import DuplicateSubmitError
import pytest


def test_idempotency_engine():
    engine = IdempotencyEngine()
    key = engine.generate_key("int1", "leg1", {"a": 1})
    engine.check_and_record(key)
    with pytest.raises(DuplicateSubmitError):
        engine.check_and_record(key)
