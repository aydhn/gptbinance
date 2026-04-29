"""Queue for risk-approved paper order intents."""
import logging
from typing import List, Optional
from datetime import datetime
from .models import PaperOrderIntent

logger = logging.getLogger(__name__)


class IntentQueue:
    def __init__(self):
        self.intents: List[PaperOrderIntent] = []
        self._processed_ids: set[str] = set()

    def enqueue(self, intent: PaperOrderIntent) -> bool:
        """Add intent to queue if not a duplicate."""
        if intent.intent_id in self._processed_ids:
            logger.debug(f"Duplicate intent rejected: {intent.intent_id}")
            return False

        self.intents.append(intent)
        self._processed_ids.add(intent.intent_id)
        return True

    def dequeue_all(self) -> List[PaperOrderIntent]:
        """Pop all intents from the queue."""
        now = datetime.utcnow()
        valid_intents = []
        for intent in self.intents:
            age = (now - intent.created_at).total_seconds()
            if age <= intent.ttl_seconds:
                valid_intents.append(intent)
            else:
                logger.warning(f"Intent expired in queue: {intent.intent_id}")

        self.intents = []
        return valid_intents

    def clear(self):
        self.intents = []
