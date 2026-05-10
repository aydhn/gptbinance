class PostmortemPlaneError(Exception):
    """Base exception for postmortem plane errors."""
    pass

class InvalidPostmortemDefinitionError(PostmortemPlaneError):
    pass

class InvalidCausalChainError(PostmortemPlaneError):
    pass

class InvalidContributorRecordError(PostmortemPlaneError):
    pass

class InvalidRemediationActionError(PostmortemPlaneError):
    pass

class VerificationViolationError(PostmortemPlaneError):
    pass

class RecurrenceViolationError(PostmortemPlaneError):
    pass

class ClosureViolationError(PostmortemPlaneError):
    pass

class EquivalenceError(PostmortemPlaneError):
    pass

class PostmortemStorageError(PostmortemPlaneError):
    pass
