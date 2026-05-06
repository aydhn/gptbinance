from app.reviews.models import ReviewRequest, ReviewScope, ReviewRequestRef
from app.reviews.enums import ReviewClass, ReviewPriority
from app.reviews.exceptions import InvalidReviewRequestError
from app.reviews.scopes import validate_scope
from typing import List, Optional
import uuid


class ReviewRequestFactory:
    @staticmethod
    def create_request(
        review_class: ReviewClass,
        scope: ReviewScope,
        rationale: str,
        producer_id: str,
        refs: Optional[List[ReviewRequestRef]] = None,
        is_high_risk: bool = False,
        requires_dual_control: bool = False,
        priority_hint: ReviewPriority = ReviewPriority.MEDIUM,
    ) -> ReviewRequest:
        validate_scope(scope)
        if not rationale:
            raise InvalidReviewRequestError("Rationale cannot be empty.")

        return ReviewRequest(
            request_id=str(uuid.uuid4()),
            review_class=review_class,
            scope=scope,
            rationale=rationale,
            producer_id=producer_id,
            refs=refs or [],
            is_high_risk=is_high_risk,
            requires_dual_control=requires_dual_control,
            priority_hint=priority_hint,
        )
