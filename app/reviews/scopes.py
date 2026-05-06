from app.reviews.models import ReviewScope
from app.reviews.exceptions import InvalidReviewRequestError


def validate_scope(scope: ReviewScope) -> bool:
    if not any(
        [
            scope.workspace_id,
            scope.profile_id,
            scope.symbol,
            scope.session_id,
            scope.candidate_id,
            scope.incident_id,
            scope.postmortem_id,
            scope.release_id,
            scope.migration_id,
        ]
    ):
        raise InvalidReviewRequestError("Scope must have at least one identifier set.")
    return True


def narrow_scope(original_scope: ReviewScope, new_scope: ReviewScope) -> ReviewScope:
    if (
        original_scope.workspace_id
        and original_scope.workspace_id != new_scope.workspace_id
    ):
        if new_scope.workspace_id is not None:
            raise InvalidReviewRequestError(
                "Cannot broaden scope or change workspace_id."
            )

    # Simple explicit narrowing logic
    return ReviewScope(
        workspace_id=original_scope.workspace_id or new_scope.workspace_id,
        profile_id=original_scope.profile_id or new_scope.profile_id,
        symbol=original_scope.symbol or new_scope.symbol,
        session_id=original_scope.session_id or new_scope.session_id,
        candidate_id=original_scope.candidate_id or new_scope.candidate_id,
        incident_id=original_scope.incident_id or new_scope.incident_id,
        postmortem_id=original_scope.postmortem_id or new_scope.postmortem_id,
        release_id=original_scope.release_id or new_scope.release_id,
        migration_id=original_scope.migration_id or new_scope.migration_id,
        narrow_explicitly=True,
    )
