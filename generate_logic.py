import os

files = {
    "app/order_lifecycle/base.py": """from abc import ABC, abstractmethod

class LifecycleOrchestratorBase(ABC):
    pass

class StateMachineBase(ABC):
    pass

class VenueEventMapperBase(ABC):
    pass

class IdempotencyGuardBase(ABC):
    pass
""",
    "app/order_lifecycle/state_machine.py": """from typing import List
from datetime import datetime, timezone
from app.order_lifecycle.enums import LifecycleState, TransitionType
from app.order_lifecycle.models import OrderLifecycleState, LifecycleTransition
from app.order_lifecycle.exceptions import InvalidLifecycleTransitionError

class LifecycleStateMachine:
    ALLOWED_TRANSITIONS = {
        LifecycleState.CREATED: [LifecycleState.READY_TO_SUBMIT],
        LifecycleState.READY_TO_SUBMIT: [LifecycleState.SUBMITTED_PENDING_ACK],
        LifecycleState.SUBMITTED_PENDING_ACK: [
            LifecycleState.ACKNOWLEDGED_OPEN,
            LifecycleState.REJECTED,
            LifecycleState.TIMEOUT_UNKNOWN,
        ],
        LifecycleState.ACKNOWLEDGED_OPEN: [
            LifecycleState.PARTIALLY_FILLED,
            LifecycleState.FULLY_FILLED,
            LifecycleState.CANCEL_REQUESTED,
            LifecycleState.REPLACE_REQUESTED,
        ],
        LifecycleState.PARTIALLY_FILLED: [
            LifecycleState.FULLY_FILLED,
            LifecycleState.CANCEL_REQUESTED,
            LifecycleState.TIMEOUT_UNKNOWN,
        ],
        LifecycleState.CANCEL_REQUESTED: [
            LifecycleState.CANCELLED,
            LifecycleState.TIMEOUT_UNKNOWN,
            LifecycleState.PARTIALLY_FILLED,
        ],
        LifecycleState.REPLACE_REQUESTED: [
            LifecycleState.REPLACED,
            LifecycleState.TIMEOUT_UNKNOWN,
            LifecycleState.REJECTED,
        ],
    }

    TERMINAL_STATES = {
        LifecycleState.FULLY_FILLED,
        LifecycleState.CANCELLED,
        LifecycleState.REJECTED,
        LifecycleState.ORPHANED,
        LifecycleState.DEAD_LETTERED,
    }

    @classmethod
    def transition(
        cls,
        attempt_id: str,
        current_state: OrderLifecycleState,
        to_state: LifecycleState,
        transition_type: TransitionType,
        explanation: str = "",
    ) -> tuple[OrderLifecycleState, LifecycleTransition]:

        if current_state.terminal:
             raise InvalidLifecycleTransitionError(f"Cannot transition from terminal state {current_state.current_state}")

        allowed_next = cls.ALLOWED_TRANSITIONS.get(current_state.current_state, [])
        if to_state not in allowed_next and to_state not in cls.TERMINAL_STATES and current_state.current_state != LifecycleState.TIMEOUT_UNKNOWN:
             raise InvalidLifecycleTransitionError(f"Invalid transition {current_state.current_state} -> {to_state}")

        now = datetime.now(timezone.utc)

        new_state = OrderLifecycleState(
            current_state=to_state,
            last_updated=now,
            terminal=to_state in cls.TERMINAL_STATES,
            unresolved=to_state == LifecycleState.TIMEOUT_UNKNOWN
        )

        transition = LifecycleTransition(
            transition_id=f"trn_{attempt_id}_{now.timestamp()}",
            attempt_id=attempt_id,
            from_state=current_state.current_state,
            to_state=to_state,
            transition_type=transition_type,
            timestamp=now,
            explanation=explanation
        )

        return new_state, transition
""",
    "app/order_lifecycle/idempotency.py": """from app.order_lifecycle.models import IdempotencyKey
from app.order_lifecycle.exceptions import DuplicateSubmitError
import hashlib
import json

class IdempotencyEngine:
    def __init__(self):
        self._seen_keys = set()

    def generate_key(self, intent_id: str, leg_id: str, context: dict) -> IdempotencyKey:
        context_str = json.dumps(context, sort_keys=True)
        raw = f"{intent_id}_{leg_id}_{context_str}"
        h = hashlib.sha256(raw.encode()).hexdigest()
        return IdempotencyKey(key=h, context=context)

    def check_and_record(self, key: IdempotencyKey):
        if key.key in self._seen_keys:
            raise DuplicateSubmitError(f"Duplicate submit attempt blocked for key {key.key}")
        self._seen_keys.add(key.key)

    def attach_existing(self, key: IdempotencyKey):
        pass
""",
    "app/order_lifecycle/client_ids.py": """import uuid

class ClientOrderIdGenerator:
    @staticmethod
    def generate(plan_id: str, leg_id: str, attempt_seq: int = 0) -> str:
        # Format compatible with strict exchanges (e.g., max 32 chars)
        short_plan = plan_id[-6:] if len(plan_id) > 6 else plan_id
        short_leg = leg_id[-6:] if len(leg_id) > 6 else leg_id
        unique = str(uuid.uuid4())[:8]
        return f"{short_plan}_{short_leg}_{attempt_seq}_{unique}"
""",
    "app/order_lifecycle/attempts.py": """from datetime import datetime, timezone
from app.order_lifecycle.models import OrderAttempt, OrderLineageRef, IdempotencyKey, OrderLifecycleState
from app.order_lifecycle.enums import LifecycleState
from app.order_lifecycle.client_ids import ClientOrderIdGenerator
from app.order_lifecycle.idempotency import IdempotencyEngine
import uuid

class AttemptManager:
    def __init__(self):
        self.idempotency_engine = IdempotencyEngine()

    def create_attempt(self, plan_id: str, leg_id: str, intent_id: str, context: dict, attempt_seq: int = 0, parent_attempt_id: str = None) -> OrderAttempt:
        client_id = ClientOrderIdGenerator.generate(plan_id, leg_id, attempt_seq)
        idem_key = self.idempotency_engine.generate_key(intent_id, leg_id, context)

        # Will raise if duplicate
        self.idempotency_engine.check_and_record(idem_key)

        return OrderAttempt(
            attempt_id=f"att_{uuid.uuid4()}",
            lineage=OrderLineageRef(
                client_order_id=client_id,
                parent_attempt_id=parent_attempt_id,
                compiled_leg_id=leg_id
            ),
            idempotency_key=idem_key,
            state=OrderLifecycleState(
                current_state=LifecycleState.CREATED,
                last_updated=datetime.now(timezone.utc)
            ),
            created_at=datetime.now(timezone.utc)
        )
""",
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
