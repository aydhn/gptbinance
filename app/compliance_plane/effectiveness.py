from app.compliance_plane.models import ControlEffectivenessReview
from typing import Dict, List


class EffectivenessManager:
    def __init__(self):
        self._reviews: Dict[str, ControlEffectivenessReview] = {}

    def register_review(self, review: ControlEffectivenessReview) -> None:
        self._reviews[review.review_id] = review

    def get_reviews_for_control(
        self, control_id: str
    ) -> List[ControlEffectivenessReview]:
        return [
            r for r in self._reviews.values() if r.control_ref.control_id == control_id
        ]

    def list_reviews(self) -> List[ControlEffectivenessReview]:
        return list(self._reviews.values())
