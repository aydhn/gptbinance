from app.order_lifecycle.models import OrderAttempt


class AttemptRepository:
    def __init__(self):
        self._db = {}

    def save(self, attempt: OrderAttempt):
        self._db[attempt.attempt_id] = attempt

    def get(self, attempt_id: str) -> OrderAttempt:
        return self._db.get(attempt_id)
