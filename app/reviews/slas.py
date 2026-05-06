from app.reviews.enums import ReviewClass, SLASeverity
from app.reviews.models import ReviewSLA
from typing import Dict

SLA_REGISTRY: Dict[ReviewClass, ReviewSLA] = {
    ReviewClass.INCIDENT_CONTAINMENT: ReviewSLA(
        review_class=ReviewClass.INCIDENT_CONTAINMENT,
        severity=SLASeverity.STRICT,
        response_timeout_minutes=15,
        completion_timeout_minutes=60,
    ),
    ReviewClass.RECOVERY_READINESS: ReviewSLA(
        review_class=ReviewClass.RECOVERY_READINESS,
        severity=SLASeverity.STRICT,
        response_timeout_minutes=30,
        completion_timeout_minutes=120,
    ),
    ReviewClass.BOARD_CONTRADICTION: ReviewSLA(
        review_class=ReviewClass.BOARD_CONTRADICTION,
        severity=SLASeverity.STANDARD,
        response_timeout_minutes=60,
        completion_timeout_minutes=240,
    ),
    ReviewClass.EVIDENCE_PACK: ReviewSLA(
        review_class=ReviewClass.EVIDENCE_PACK,
        severity=SLASeverity.RELAXED,
        response_timeout_minutes=24 * 60,
        completion_timeout_minutes=48 * 60,
    ),
}


def get_sla_for_class(review_class: ReviewClass) -> ReviewSLA:
    return SLA_REGISTRY.get(
        review_class,
        ReviewSLA(
            review_class=review_class,
            severity=SLASeverity.STANDARD,
            response_timeout_minutes=60,
            completion_timeout_minutes=24 * 60,
        ),
    )
