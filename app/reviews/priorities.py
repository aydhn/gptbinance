from app.reviews.enums import ReviewPriority, ReviewClass
from app.reviews.models import ReviewRequest


def calculate_priority(request: ReviewRequest) -> ReviewPriority:
    if request.is_high_risk:
        return ReviewPriority.CRITICAL

    if request.review_class in [
        ReviewClass.INCIDENT_CONTAINMENT,
        ReviewClass.RECOVERY_READINESS,
        ReviewClass.ACTIVATION_HALT,
    ]:
        return ReviewPriority.CRITICAL

    if request.review_class in [
        ReviewClass.BOARD_CONTRADICTION,
        ReviewClass.MIGRATION_NON_REVERSIBLE,
        ReviewClass.RELEASE_HOLD,
        ReviewClass.RELIABILITY_FREEZE,
    ]:
        return ReviewPriority.HIGH

    return request.priority_hint
