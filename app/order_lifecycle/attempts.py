from datetime import datetime, timezone
from app.order_lifecycle.models import (
    OrderAttempt,
    OrderLineageRef,
    IdempotencyKey,
    OrderLifecycleState,
)
from app.order_lifecycle.enums import LifecycleState
from app.order_lifecycle.client_ids import ClientOrderIdGenerator
from app.order_lifecycle.idempotency import IdempotencyEngine
import uuid


class AttemptManager:
    def __init__(self):
        self.idempotency_engine = IdempotencyEngine()

    def create_attempt(
        self,
        plan_id: str,
        leg_id: str,
        intent_id: str,
        context: dict,
        attempt_seq: int = 0,
        parent_attempt_id: str = None,
    ) -> OrderAttempt:
        client_id = ClientOrderIdGenerator.generate(plan_id, leg_id, attempt_seq)
        idem_key = self.idempotency_engine.generate_key(intent_id, leg_id, context)

        # Will raise if duplicate
        self.idempotency_engine.check_and_record(idem_key)

        return OrderAttempt(
            attempt_id=f"att_{uuid.uuid4()}",
            lineage=OrderLineageRef(
                client_order_id=client_id,
                parent_attempt_id=parent_attempt_id,
                compiled_leg_id=leg_id,
            ),
            idempotency_key=idem_key,
            state=OrderLifecycleState(
                current_state=LifecycleState.CREATED,
                last_updated=datetime.now(timezone.utc),
            ),
            created_at=datetime.now(timezone.utc),
        )
