from app.order_lifecycle.models import IdempotencyKey
from app.order_lifecycle.exceptions import DuplicateSubmitError
import hashlib
import json


class IdempotencyEngine:
    def __init__(self):
        self._seen_keys = set()

    def generate_key(
        self, intent_id: str, leg_id: str, context: dict
    ) -> IdempotencyKey:
        context_str = json.dumps(context, sort_keys=True)
        raw = f"{intent_id}_{leg_id}_{context_str}"
        h = hashlib.sha256(raw.encode()).hexdigest()
        return IdempotencyKey(key=h, context=context)

    def check_and_record(self, key: IdempotencyKey):
        if key.key in self._seen_keys:
            raise DuplicateSubmitError(
                f"Duplicate submit attempt blocked for key {key.key}"
            )
        self._seen_keys.add(key.key)

    def attach_existing(self, key: IdempotencyKey):
        pass
