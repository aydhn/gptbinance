class ReviewFabricError(Exception):
    pass


class InvalidReviewRequestError(ReviewFabricError):
    pass


class InvalidQueueItemError(ReviewFabricError):
    pass


class InvalidAssignmentError(ReviewFabricError):
    pass


class SeparationOfDutiesViolation(ReviewFabricError):
    pass


class ChecklistIncompleteError(ReviewFabricError):
    pass


class AdjudicationError(ReviewFabricError):
    pass


class EscalationError(ReviewFabricError):
    pass


class StaleReviewError(ReviewFabricError):
    pass


class ReviewStorageError(ReviewFabricError):
    pass
