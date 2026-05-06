from typing import Dict, List, Optional
from app.reviews.enums import QueueClass, ReviewClass, ReviewPriority, ReviewState
from app.reviews.models import ReviewRequest, QueueItem, ReviewQueue
from app.reviews.priorities import calculate_priority
import uuid

QUEUE_MAPPING: Dict[ReviewClass, QueueClass] = {
    ReviewClass.POLICY_CONFLICT: QueueClass.POLICY,
    ReviewClass.BOARD_CONTRADICTION: QueueClass.READINESS_BOARD,
    ReviewClass.ACTIVATION_EXPANSION: QueueClass.ACTIVATION,
    ReviewClass.ACTIVATION_HALT: QueueClass.ACTIVATION,
    ReviewClass.INCIDENT_CONTAINMENT: QueueClass.INCIDENTS,
    ReviewClass.RECOVERY_READINESS: QueueClass.INCIDENTS,
    ReviewClass.POSTMORTEM_FINALIZE: QueueClass.POSTMORTEMS,
    ReviewClass.CAPA_EFFECTIVENESS: QueueClass.POSTMORTEMS,
    ReviewClass.MIGRATION_SCOPE: QueueClass.MIGRATIONS,
    ReviewClass.MIGRATION_NON_REVERSIBLE: QueueClass.MIGRATIONS,
    ReviewClass.REMEDIATION_APPLY: QueueClass.REMEDIATION,
    ReviewClass.EVIDENCE_PACK: QueueClass.GENERAL,
    ReviewClass.RELEASE_HOLD: QueueClass.RELEASE,
    ReviewClass.RELIABILITY_FREEZE: QueueClass.RELIABILITY,
}


class QueueEngine:
    def __init__(self):
        self._queues: Dict[str, ReviewQueue] = {}
        self._items: Dict[str, QueueItem] = {}

        for q_class in QueueClass:
            q_id = str(uuid.uuid4())
            self._queues[q_id] = ReviewQueue(
                queue_id=q_id,
                queue_class=q_class,
                name=f"{q_class.value.capitalize()} Queue",
                description=f"Queue for {q_class.value} reviews.",
            )

    def _get_queue_by_class(self, q_class: QueueClass) -> Optional[ReviewQueue]:
        for q in self._queues.values():
            if q.queue_class == q_class:
                return q
        return None

    def enqueue(self, request: ReviewRequest) -> QueueItem:
        q_class = QUEUE_MAPPING.get(request.review_class, QueueClass.GENERAL)
        queue = self._get_queue_by_class(q_class)
        if not queue:
            raise ValueError(f"No queue found for {q_class}")

        priority = calculate_priority(request)

        item = QueueItem(
            item_id=str(uuid.uuid4()),
            queue_id=queue.queue_id,
            request=request,
            priority=priority,
        )
        self._items[item.item_id] = item
        return item

    def get_pending_items(self, queue_id: Optional[str] = None) -> List[QueueItem]:
        items = [
            i
            for i in self._items.values()
            if i.state in [ReviewState.PENDING, ReviewState.ASSIGNED]
        ]
        if queue_id:
            items = [i for i in items if i.queue_id == queue_id]

        # Sort by priority and then queued_at
        priority_order = {
            ReviewPriority.CRITICAL: 0,
            ReviewPriority.HIGH: 1,
            ReviewPriority.MEDIUM: 2,
            ReviewPriority.LOW: 3,
        }
        items.sort(key=lambda x: (priority_order[x.priority], x.queued_at))
        return items

    def get_item(self, item_id: str) -> Optional[QueueItem]:
        return self._items.get(item_id)

    def update_item_state(self, item_id: str, state: ReviewState):
        if item_id in self._items:
            self._items[item_id].state = state
