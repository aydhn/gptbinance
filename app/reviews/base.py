from abc import ABC, abstractmethod
from typing import List, Optional
from app.reviews.models import (
    ReviewRequest,
    QueueItem,
    ReviewDecisionRecord,
    ReviewEscalation,
)


class ReviewIntakeBase(ABC):
    @abstractmethod
    def submit_request(self, request: ReviewRequest) -> QueueItem:
        pass


class QueueEngineBase(ABC):
    @abstractmethod
    def enqueue(self, request: ReviewRequest) -> QueueItem:
        pass

    @abstractmethod
    def get_pending_items(self, queue_id: str) -> List[QueueItem]:
        pass


class AdjudicationEngineBase(ABC):
    @abstractmethod
    def adjudicate(
        self, item_id: str, adjudicator_id: str, verdict: str, rationale: str
    ) -> ReviewDecisionRecord:
        pass


class EscalationEngineBase(ABC):
    @abstractmethod
    def escalate(
        self, item_id: str, reason: str, escalated_by: str
    ) -> ReviewEscalation:
        pass
