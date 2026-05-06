from typing import Dict, List
from app.reviews.models import ReviewRequest, QueueItem, ReviewDecisionRecord


class InMemoryReviewStorage:
    def __init__(self):
        self.requests: Dict[str, ReviewRequest] = {}
        self.items: Dict[str, QueueItem] = {}
        self.decisions: Dict[str, ReviewDecisionRecord] = {}

    def save_request(self, request: ReviewRequest):
        self.requests[request.request_id] = request

    def save_item(self, item: QueueItem):
        self.items[item.item_id] = item

    def save_decision(self, decision: ReviewDecisionRecord):
        self.decisions[decision.decision_id] = decision

    def get_item(self, item_id: str) -> QueueItem:
        return self.items.get(item_id)
