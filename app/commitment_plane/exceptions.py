class CommitmentPlaneError(Exception):
    """Base exception for Commitment Plane"""
    pass

class InvalidCommitmentObjectError(CommitmentPlaneError):
    pass

class InvalidBindingDefinitionError(CommitmentPlaneError):
    pass

class InvalidOwnerAssignmentError(CommitmentPlaneError):
    pass

class InvalidDeadlineSemanticsError(CommitmentPlaneError):
    pass

class InvalidReliefError(CommitmentPlaneError):
    pass

class InvalidDischargeError(CommitmentPlaneError):
    pass

class BreachIntegrityViolationError(CommitmentPlaneError):
    pass

class CommitmentStorageError(CommitmentPlaneError):
    pass
