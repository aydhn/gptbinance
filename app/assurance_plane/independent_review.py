from app.assurance_plane.models import IndependentReviewRecord

def create_independent_review(review_id: str, assurance_id: str, reviewer: str, is_clean: bool, notes: str) -> IndependentReviewRecord:
    return IndependentReviewRecord(
        review_id=review_id,
        assurance_id=assurance_id,
        reviewer=reviewer,
        is_clean=is_clean,
        notes=notes
    )
